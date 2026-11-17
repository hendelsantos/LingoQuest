import re

from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .grading import is_close, is_equivalent
from .models import Course, Lesson, Question
from .serializers import (
    AnswerFeedbackSerializer,
    AnswerRequestSerializer,
    CourseOutlineSerializer,
    CourseSummarySerializer,
    LessonDetailSerializer,
)


def lesson_summary(lesson: Lesson) -> dict:
    return {
        "slug": lesson.slug,
        "title": lesson.title,
        "skill": lesson.skill,
        "summary": lesson.summary,
        "estimatedMinutes": lesson.estimated_minutes,
        "xpReward": lesson.xp_reward,
        "position": lesson.position,
    }


class DemoCoursesListView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(responses=CourseSummarySerializer(many=True))
    def get(self, request):
        published_lessons = Lesson.objects.filter(status=Lesson.Status.PUBLISHED)
        courses = (
            Course.objects.filter(status=Course.Status.PUBLISHED)
            .prefetch_related(Prefetch("units__lessons", queryset=published_lessons))
            .order_by("level")
        )
        data = [
            {
                "slug": course.slug,
                "title": course.title,
                "description": course.description,
                "level": course.level,
                "unitCount": course.units.count(),
                "lessonCount": sum(unit.lessons.count() for unit in course.units.all()),
            }
            for course in courses
        ]
        return Response(data)


class DemoCourseOutlineView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(responses=CourseOutlineSerializer)
    def get(self, request, slug: str):
        published_lessons = Lesson.objects.filter(status=Lesson.Status.PUBLISHED).order_by(
            "position"
        )
        course = get_object_or_404(
            Course.objects.filter(status=Course.Status.PUBLISHED).prefetch_related(
                Prefetch("units__lessons", queryset=published_lessons)
            ),
            slug=slug,
        )
        units = [
            {
                "title": unit.title,
                "description": unit.description,
                "position": unit.position,
                "lessons": [lesson_summary(lesson) for lesson in unit.lessons.all()],
            }
            for unit in course.units.all()
        ]
        return Response(
            {
                "slug": course.slug,
                "title": course.title,
                "description": course.description,
                "level": course.level,
                "lessonCount": sum(len(unit["lessons"]) for unit in units),
                "units": units,
            }
        )


def question_payload(question: Question) -> dict:
    payload = {
        "id": question.id,
        "type": question.type,
        "prompt": question.prompt,
        "position": question.position,
    }
    if question.type == Question.Type.MCQ:
        payload["choices"] = [
            {"id": choice.id, "text": choice.text, "position": choice.position}
            for choice in question.choices.all()
        ]
    elif question.type == Question.Type.ORDERING:
        tokens = question.answer_data.get("tokens")
        if not tokens:
            correct = question.answer_data.get("correct", "")
            tokens = [
                re.sub(r"[.?!]+$", "", word) for word in correct.split() if word.strip()
            ]
        payload["tokens"] = tokens
    elif question.type == Question.Type.LISTENING:
        # O texto é necessário para o navegador sintetizar o áudio (TTS).
        payload["audioText"] = question.answer_data.get("correct", "")
    return payload


class DemoLessonDetailView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(responses=LessonDetailSerializer)
    def get(self, request, slug: str):
        lesson = get_object_or_404(
            Lesson.objects.filter(
                slug=slug,
                status=Lesson.Status.PUBLISHED,
                unit__course__status=Course.Status.PUBLISHED,
            ).prefetch_related("questions__choices"),
        )
        return Response(
            {
                **lesson_summary(lesson),
                "unit": lesson.unit.title,
                "theory": lesson.theory,
                "example": lesson.example,
                "keyPoints": lesson.key_points,
                "dialogue": lesson.dialogue,
                "passingPercent": lesson.passing_percent,
                "questions": [
                    question_payload(question) for question in lesson.questions.all()
                ],
            }
        )


class InvalidAnswer(Exception):
    code = "INVALID_ANSWER"
    detail = "Envie uma resposta válida."

    def __init__(self, *, code: str | None = None, detail: str | None = None) -> None:
        if code is not None:
            self.code = code
        if detail is not None:
            self.detail = detail
        super().__init__(self.detail)


def grade_answer(question: Question, data: dict) -> dict:
    """Compara a resposta enviada com o gabarito, conforme o tipo da questão."""
    explanation = question.explanation

    if question.type == Question.Type.MCQ:
        selected = next(
            (choice for choice in question.choices.all() if choice.id == data["choiceId"]),
            None,
        )
        if selected is None:
            raise InvalidAnswer(code="CHOICE_NOT_AVAILABLE", detail="Alternativa inválida.")
        correct = next(choice for choice in question.choices.all() if choice.is_correct)
        return {
            "isCorrect": selected.is_correct,
            "selectedChoiceId": selected.id,
            "correctChoiceId": correct.id,
            "explanation": explanation,
        }

    correct = str(question.answer_data.get("correct", "")).strip()
    if not correct:
        raise InvalidAnswer()

    if question.type == Question.Type.ORDERING:
        order = data.get("order")
        if not isinstance(order, list) or not order:
            raise InvalidAnswer(detail="Organize as palavras antes de confirmar.")
        answer = " ".join(str(token).strip() for token in order if str(token).strip())
        return {
            "isCorrect": is_equivalent(answer, correct),
            "correctAnswer": correct,
            "explanation": explanation,
        }

    answer = data.get("answer")
    if not isinstance(answer, str) or not answer.strip():
        raise InvalidAnswer()

    if question.type == Question.Type.LISTENING:
        return {
            "isCorrect": is_close(answer, correct),
            "correctAnswer": correct,
            "explanation": explanation,
        }

    accepted = question.answer_data.get("accepted") or [correct]
    is_correct = any(is_equivalent(candidate, answer) for candidate in accepted)
    return {"isCorrect": is_correct, "correctAnswer": correct, "explanation": explanation}


class DemoAnswerView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(request=AnswerRequestSerializer, responses=AnswerFeedbackSerializer)
    def post(self, request, slug: str):
        question_id = request.data.get("questionId")
        if not question_id:
            return Response(
                {"code": "INVALID_ANSWER", "detail": "Resposta incompleta."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        question = get_object_or_404(
            Question.objects.prefetch_related("choices").filter(
                id=question_id,
                lesson__slug=slug,
                lesson__status=Lesson.Status.PUBLISHED,
                lesson__unit__course__status=Course.Status.PUBLISHED,
            )
        )

        data = {
            "choiceId": request.data.get("choiceId"),
            "answer": request.data.get("answer"),
            "order": request.data.get("order"),
        }

        try:
            feedback = grade_answer(question, data)
        except InvalidAnswer as exc:
            return Response(
                {"code": exc.code, "detail": exc.detail},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(feedback)
