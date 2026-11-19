import re

from django.db import IntegrityError, transaction
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User
from apps.accounts.permissions import IsAdminRole, IsStudentRole

from .content.assessments import ASSESSMENTS
from .grading import is_close, is_equivalent, similarity
from .models import Course, Enrollment, Lesson, Question
from .serializers import (
    AnswerFeedbackSerializer,
    AnswerRequestSerializer,
    AssessmentAnswerSerializer,
    AssessmentDetailSerializer,
    AssessmentFeedbackSerializer,
    CourseOutlineSerializer,
    CourseSummarySerializer,
    EnrollmentCreateSerializer,
    EnrollmentSerializer,
    EnrollmentStatusSerializer,
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


def course_outline_payload(course: Course) -> dict:
    units = [
        {
            "title": unit.title,
            "description": unit.description,
            "position": unit.position,
            "lessons": [lesson_summary(lesson) for lesson in unit.lessons.all()],
        }
        for unit in course.units.all()
    ]
    return {
        "slug": course.slug,
        "title": course.title,
        "description": course.description,
        "level": course.level,
        "lessonCount": sum(len(unit["lessons"]) for unit in units),
        "units": units,
    }


def lesson_detail_payload(lesson: Lesson) -> dict:
    return {
        **lesson_summary(lesson),
        "unit": lesson.unit.title,
        "theory": lesson.theory,
        "example": lesson.example,
        "keyPoints": lesson.key_points,
        "dialogue": lesson.dialogue,
        **(
            {
                "pedagogy": {
                    "objective": lesson.pedagogy["objective"],
                    "activationPrompt": lesson.pedagogy["activation_prompt"],
                    "commonMistakes": lesson.pedagogy["common_mistakes"],
                    "productionTask": {
                        "mode": lesson.pedagogy["production_task"]["mode"],
                        "prompt": lesson.pedagogy["production_task"]["prompt"],
                        "model": lesson.pedagogy["production_task"]["model"],
                        "checklist": lesson.pedagogy["production_task"]["checklist"],
                    },
                    "reviewPrompts": lesson.pedagogy["review_prompts"],
                }
            }
            if lesson.pedagogy
            else {}
        ),
        "passingPercent": lesson.passing_percent,
        "questions": [question_payload(question) for question in lesson.questions.all()],
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
        return Response(course_outline_payload(course))


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
        return Response(lesson_detail_payload(lesson))


ACCESSIBLE_ENROLLMENT_STATUSES = (
    Enrollment.Status.ACTIVE,
    Enrollment.Status.COMPLETED,
)


def enrollment_payload(enrollment: Enrollment) -> dict:
    return {
        "id": enrollment.id,
        "student": {
            "id": enrollment.student_id,
            "name": enrollment.student.name,
            "email": enrollment.student.email,
        },
        "course": {
            "slug": enrollment.course.slug,
            "title": enrollment.course.title,
            "level": enrollment.course.level,
        },
        "status": enrollment.status,
        "enrolledAt": enrollment.enrolled_at,
        "endedAt": enrollment.ended_at,
    }


def enrolled_courses(user: User):
    return Course.objects.filter(
        status=Course.Status.PUBLISHED,
        enrollments__student=user,
        enrollments__status__in=ACCESSIBLE_ENROLLMENT_STATUSES,
    )


class StudentEnrollmentListView(APIView):
    permission_classes = (IsStudentRole,)

    @extend_schema(responses=EnrollmentSerializer(many=True))
    def get(self, request):
        enrollments = Enrollment.objects.filter(student=request.user).select_related(
            "student", "course"
        )
        return Response([enrollment_payload(item) for item in enrollments])


class AuthorizedCourseOutlineView(APIView):
    permission_classes = (IsStudentRole,)

    @extend_schema(responses=CourseOutlineSerializer)
    def get(self, request, slug: str):
        published_lessons = Lesson.objects.filter(
            status=Lesson.Status.PUBLISHED
        ).order_by("position")
        course = get_object_or_404(
            enrolled_courses(request.user).prefetch_related(
                Prefetch("units__lessons", queryset=published_lessons)
            ),
            slug=slug,
        )
        return Response(course_outline_payload(course))


class AuthorizedLessonDetailView(APIView):
    permission_classes = (IsStudentRole,)

    @extend_schema(responses=LessonDetailSerializer)
    def get(self, request, slug: str):
        lesson = get_object_or_404(
            Lesson.objects.filter(
                slug=slug,
                status=Lesson.Status.PUBLISHED,
                unit__course__in=enrolled_courses(request.user),
            ).prefetch_related("questions__choices"),
        )
        return Response(lesson_detail_payload(lesson))


class AdminEnrollmentListCreateView(APIView):
    permission_classes = (IsAdminRole,)

    @extend_schema(responses=EnrollmentSerializer(many=True))
    def get(self, request):
        enrollments = Enrollment.objects.select_related("student", "course")
        return Response([enrollment_payload(item) for item in enrollments])

    @extend_schema(
        request=EnrollmentCreateSerializer,
        responses={201: EnrollmentSerializer},
    )
    def post(self, request):
        serializer = EnrollmentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                enrollment = Enrollment.objects.create(
                    student_id=serializer.validated_data["studentId"],
                    course=Course.objects.get(
                        slug=serializer.validated_data["courseSlug"]
                    ),
                )
        except IntegrityError:
            return Response(
                {
                    "code": "ENROLLMENT_ALREADY_EXISTS",
                    "detail": "Este aluno já possui matrícula neste curso.",
                },
                status=status.HTTP_409_CONFLICT,
            )
        enrollment = Enrollment.objects.select_related("student", "course").get(
            id=enrollment.id
        )
        return Response(enrollment_payload(enrollment), status=status.HTTP_201_CREATED)


class AdminEnrollmentDetailView(APIView):
    permission_classes = (IsAdminRole,)

    @extend_schema(
        request=EnrollmentStatusSerializer,
        responses=EnrollmentSerializer,
    )
    def patch(self, request, enrollment_id):
        serializer = EnrollmentStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            enrollment = get_object_or_404(
                Enrollment.objects.select_for_update().select_related("student", "course"),
                id=enrollment_id,
            )
            enrollment.status = serializer.validated_data["status"]
            enrollment.ended_at = (
                timezone.now()
                if enrollment.status
                in {Enrollment.Status.COMPLETED, Enrollment.Status.CANCELLED}
                else None
            )
            enrollment.save(update_fields=("status", "ended_at"))
        return Response(enrollment_payload(enrollment))


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


def error_category(question: Question, data: dict) -> str:
    if question.type == Question.Type.LISTENING:
        return "LISTENING"
    if question.type == Question.Type.ORDERING:
        return "WORD_ORDER"
    if question.type == Question.Type.FILL_IN:
        answer = data.get("answer")
        correct = str(question.answer_data.get("correct", ""))
        if isinstance(answer, str) and correct and similarity(answer, correct) >= 0.9:
            return "SPELLING"
    if question.lesson.skill == "Vocabulary":
        return "VOCABULARY"
    if question.lesson.skill in {"Conversation", "Speaking", "Review"}:
        return "COMPREHENSION"
    return "GRAMMAR"


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

        if not feedback["isCorrect"]:
            feedback["errorCategory"] = error_category(question, data)

        return Response(feedback)


class AuthorizedAnswerView(APIView):
    permission_classes = (IsStudentRole,)

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
                lesson__unit__course__in=enrolled_courses(request.user),
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
        if not feedback["isCorrect"]:
            feedback["errorCategory"] = error_category(question, data)
        return Response(feedback)


def assessment_payload(moment: str, assessment: dict) -> dict:
    questions = []
    for question in assessment["questions"]:
        payload = {
            "id": question["id"],
            "type": question["type"],
            "prompt": question["prompt"],
        }
        if question["type"] == "MCQ":
            payload["choices"] = question["choices"]
        elif question["type"] == "ORDERING":
            words = [re.sub(r"[.?!]+$", "", word) for word in question["correct"].split()]
            payload["tokens"] = words[len(words) // 2 :] + words[: len(words) // 2]
        elif question["type"] == "LISTENING":
            payload["audioText"] = question["correct"]
        questions.append(payload)
    return {
        "moment": moment,
        "title": assessment["title"],
        "description": assessment["description"],
        "questions": questions,
        "speakingTask": assessment["speakingTask"],
        "writingTask": assessment["writingTask"],
    }


class DemoAssessmentDetailView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(responses=AssessmentDetailSerializer)
    def get(self, request, moment: str):
        assessment = ASSESSMENTS.get(moment)
        if assessment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(assessment_payload(moment, assessment))


class DemoAssessmentAnswerView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        request=AssessmentAnswerSerializer,
        responses={200: AssessmentFeedbackSerializer},
    )
    def post(self, request, moment: str):
        assessment = ASSESSMENTS.get(moment)
        if assessment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AssessmentAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = next(
            (
                item
                for item in assessment["questions"]
                if item["id"] == serializer.validated_data["questionId"]
            ),
            None,
        )
        if question is None:
            return Response(
                {"detail": "Questão inválida."}, status=status.HTTP_400_BAD_REQUEST
            )

        qtype = question["type"]
        if qtype == "MCQ":
            choice_index = serializer.validated_data.get("choiceIndex")
            correct = choice_index == question["correct_index"]
            feedback = {
                "isCorrect": correct,
                "correctChoiceIndex": question["correct_index"],
                "explanation": question["explanation"],
            }
        else:
            if qtype == "ORDERING":
                candidate = " ".join(serializer.validated_data.get("order", []))
                correct = is_equivalent(candidate, question["correct"])
            elif qtype == "LISTENING":
                correct = is_close(
                    serializer.validated_data.get("answer", ""), question["correct"]
                )
            else:
                answer = serializer.validated_data.get("answer", "")
                correct = any(
                    is_equivalent(answer, accepted)
                    for accepted in question.get("accepted", [question["correct"]])
                )
            feedback = {
                "isCorrect": correct,
                "correctAnswer": question["correct"],
                "explanation": question["explanation"],
            }
        if not correct:
            feedback["errorCategory"] = question["category"]
        return Response(feedback)
