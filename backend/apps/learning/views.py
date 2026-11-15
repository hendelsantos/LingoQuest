from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Lesson, Question
from .serializers import (
    AnswerFeedbackSerializer,
    AnswerRequestSerializer,
    CourseOutlineSerializer,
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
                "passingPercent": lesson.passing_percent,
                "questions": [
                    {
                        "id": question.id,
                        "prompt": question.prompt,
                        "position": question.position,
                        "choices": [
                            {"id": choice.id, "text": choice.text, "position": choice.position}
                            for choice in question.choices.all()
                        ],
                    }
                    for question in lesson.questions.all()
                ],
            }
        )


class DemoAnswerView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(request=AnswerRequestSerializer, responses=AnswerFeedbackSerializer)
    def post(self, request, slug: str):
        question_id = request.data.get("questionId")
        choice_id = request.data.get("choiceId")
        if not question_id or not choice_id:
            return Response(
                {"code": "INVALID_ANSWER", "detail": "Escolha uma alternativa."},
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
        selected = next(
            (choice for choice in question.choices.all() if choice.id == choice_id), None
        )
        if selected is None:
            return Response(
                {"code": "CHOICE_NOT_AVAILABLE", "detail": "Alternativa inválida."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        correct = next(choice for choice in question.choices.all() if choice.is_correct)
        return Response(
            {
                "isCorrect": selected.is_correct,
                "selectedChoiceId": selected.id,
                "correctChoiceId": correct.id,
                "explanation": question.explanation,
            }
        )
