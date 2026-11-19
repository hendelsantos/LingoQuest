from dataclasses import dataclass

from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from apps.gamification.models import XPEvent

from .grading import error_category, grade_answer
from .models import (
    AttemptAnswer,
    Enrollment,
    Lesson,
    LessonAttempt,
    LessonProgress,
    Question,
)


@dataclass
class AttemptStateError(Exception):
    code: str
    detail: str


ACCESSIBLE_ENROLLMENT_STATUSES = (
    Enrollment.Status.ACTIVE,
    Enrollment.Status.COMPLETED,
)


def _lock_accessible_enrollment(*, student, lesson: Lesson) -> None:
    if not Enrollment.objects.select_for_update().filter(
        student=student,
        course=lesson.unit.course,
        status__in=ACCESSIBLE_ENROLLMENT_STATUSES,
    ).exists():
        raise AttemptStateError(
            code="LESSON_NOT_AVAILABLE",
            detail="Esta lição não está disponível.",
        )


@transaction.atomic
def start_or_resume_attempt(*, student, lesson: Lesson) -> LessonAttempt:
    """Serializa inícios pela matrícula e devolve a tentativa ativa existente."""
    _lock_accessible_enrollment(student=student, lesson=lesson)

    current = LessonAttempt.objects.filter(
        student=student,
        lesson=lesson,
        status=LessonAttempt.Status.IN_PROGRESS,
    ).first()
    if current is not None:
        return current
    return LessonAttempt.objects.create(student=student, lesson=lesson)


def _normalized_response(question: Question, data: dict, feedback: dict) -> dict:
    if question.type == Question.Type.MCQ:
        return {"choiceId": feedback["selectedChoiceId"]}
    if question.type == Question.Type.ORDERING:
        return {
            "order": [str(token).strip() for token in data.get("order", []) if str(token).strip()]
        }
    return {"answer": str(data.get("answer", ""))}


@transaction.atomic
def confirm_attempt_answer(
    *,
    attempt_id,
    student,
    question_id: int,
    data: dict,
) -> AttemptAnswer:
    attempt_reference = LessonAttempt.objects.select_related("lesson__unit__course").get(
        id=attempt_id,
        student=student,
    )
    _lock_accessible_enrollment(student=student, lesson=attempt_reference.lesson)
    attempt = (
        LessonAttempt.objects.select_for_update()
        .select_related("lesson__unit__course")
        .get(id=attempt_id, student=student)
    )
    if attempt.status != LessonAttempt.Status.IN_PROGRESS:
        raise AttemptStateError(
            code="ATTEMPT_ALREADY_FINISHED",
            detail="Esta tentativa já foi finalizada.",
        )

    question = (
        Question.objects.filter(id=question_id, lesson=attempt.lesson)
        .prefetch_related("choices")
        .first()
    )
    if question is None:
        raise AttemptStateError(
            code="QUESTION_NOT_AVAILABLE",
            detail="Esta pergunta não pertence à tentativa.",
        )

    feedback = grade_answer(question, data)
    if not feedback["isCorrect"]:
        feedback["errorCategory"] = error_category(question, data)
    response_data = _normalized_response(question, data, feedback)

    existing = AttemptAnswer.objects.filter(attempt=attempt, question=question).first()
    if existing is not None:
        if existing.response_data == response_data:
            return existing
        raise AttemptStateError(
            code="ANSWER_ALREADY_CONFIRMED",
            detail="A resposta desta pergunta já foi confirmada.",
        )

    return AttemptAnswer.objects.create(
        attempt=attempt,
        question=question,
        selected_choice_id=feedback.get("selectedChoiceId"),
        response_data=response_data,
        feedback=feedback,
        is_correct=feedback["isCorrect"],
    )


@transaction.atomic
def finish_attempt(*, attempt_id, student) -> LessonAttempt:
    attempt_reference = LessonAttempt.objects.select_related("lesson__unit__course").get(
        id=attempt_id,
        student=student,
    )
    _lock_accessible_enrollment(student=student, lesson=attempt_reference.lesson)
    attempt = (
        LessonAttempt.objects.select_for_update()
        .select_related("lesson__unit__course")
        .get(id=attempt_id, student=student)
    )
    if attempt.status == LessonAttempt.Status.SUBMITTED:
        return attempt
    if attempt.status != LessonAttempt.Status.IN_PROGRESS:
        raise AttemptStateError(
            code="ATTEMPT_NOT_ACTIVE",
            detail="Esta tentativa não pode mais ser finalizada.",
        )

    questions = list(attempt.lesson.questions.all())
    answers = list(attempt.answers.select_related("question").all())
    if len(answers) != len(questions):
        raise AttemptStateError(
            code="ATTEMPT_INCOMPLETE",
            detail="Responda todas as perguntas antes de finalizar.",
        )

    total_weight = sum(question.weight for question in questions)
    correct_weight = sum(answer.question.weight for answer in answers if answer.is_correct)
    correct_count = sum(1 for answer in answers if answer.is_correct)
    score_percent = round(correct_weight * 100 / total_weight) if total_weight else 0
    passed = bool(
        total_weight
        and correct_weight * 100 >= attempt.lesson.passing_percent * total_weight
    )
    finished_at = timezone.now()

    progress = (
        LessonProgress.objects.select_for_update()
        .filter(student=student, lesson=attempt.lesson)
        .first()
    )
    if progress is None:
        progress = LessonProgress(
            student=student,
            lesson=attempt.lesson,
            last_attempt_at=finished_at,
        )
    progress.best_score = max(progress.best_score, score_percent)
    progress.last_attempt_at = finished_at
    if passed and not progress.completed:
        progress.completed = True
        progress.first_passed_at = finished_at
    progress.save()

    xp_awarded = 0
    if passed:
        _event, created = XPEvent.objects.get_or_create(
            student=student,
            source_type=XPEvent.SourceType.LESSON_COMPLETION,
            source_id=str(attempt.lesson_id),
            defaults={"amount": attempt.lesson.xp_reward},
        )
        if created:
            xp_awarded = attempt.lesson.xp_reward

    attempt.status = LessonAttempt.Status.SUBMITTED
    attempt.submitted_at = finished_at
    attempt.correct_count = correct_count
    attempt.total_questions = len(questions)
    attempt.score_percent = score_percent
    attempt.passed = passed
    attempt.xp_awarded = xp_awarded
    attempt.save(
        update_fields=(
            "status",
            "submitted_at",
            "correct_count",
            "total_questions",
            "score_percent",
            "passed",
            "xp_awarded",
        )
    )
    return attempt


def attempt_answer_payload(answer: AttemptAnswer) -> dict:
    return {
        "questionId": answer.question_id,
        **answer.response_data,
        **answer.feedback,
        "answeredAt": answer.answered_at,
    }


def attempt_payload(attempt: LessonAttempt) -> dict:
    answers = list(attempt.answers.select_related("question").all())
    return {
        "id": attempt.id,
        "lessonSlug": attempt.lesson.slug,
        "status": attempt.status,
        "startedAt": attempt.started_at,
        "submittedAt": attempt.submitted_at,
        "answeredCount": len(answers),
        "correctCount": (
            attempt.correct_count
            if attempt.status == LessonAttempt.Status.SUBMITTED
            else sum(1 for answer in answers if answer.is_correct)
        ),
        "totalQuestions": (
            attempt.total_questions
            if attempt.status == LessonAttempt.Status.SUBMITTED
            else attempt.lesson.questions.count()
        ),
        "scorePercent": attempt.score_percent,
        "passed": attempt.passed,
        "xpAwarded": attempt.xp_awarded,
        "answers": [attempt_answer_payload(answer) for answer in answers],
    }


def student_learning_summary(student) -> dict:
    enrollments = Enrollment.objects.filter(
        student=student,
        status__in=ACCESSIBLE_ENROLLMENT_STATUSES,
    )
    required_lessons = Lesson.objects.filter(
        unit__course__enrollments__in=enrollments,
        status=Lesson.Status.PUBLISHED,
        required=True,
    ).distinct()
    completed_count = LessonProgress.objects.filter(
        student=student,
        lesson__in=required_lessons,
        completed=True,
    ).count()
    total_lessons = required_lessons.count()
    total_xp = (
        XPEvent.objects.filter(student=student).aggregate(total=Sum("amount"))["total"] or 0
    )
    return {
        "xp": total_xp,
        "completedLessons": completed_count,
        "totalLessons": total_lessons,
        "progressPercent": (
            round(completed_count * 100 / total_lessons) if total_lessons else 0
        ),
    }
