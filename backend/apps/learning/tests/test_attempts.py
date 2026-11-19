from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

import pytest
from django.db import connections
from django.urls import reverse
from rest_framework.test import APIClient

from apps.accounts.models import User
from apps.gamification.models import XPEvent
from apps.learning.attempts import finish_attempt
from apps.learning.models import (
    Choice,
    Course,
    Enrollment,
    LessonAttempt,
    LessonProgress,
    Question,
)
from apps.learning.services import seed_curriculum


@pytest.fixture
def published_course(db):
    seed_curriculum()
    return Course.objects.get(slug="a1-foundations")


@pytest.fixture
def users(db):
    return {
        "student": User.objects.create_user(
            email="student-attempts@example.com",
            name="Student",
            role=User.Role.STUDENT,
            password="safe-test-password",
        ),
        "other": User.objects.create_user(
            email="other-attempts@example.com",
            name="Other Student",
            role=User.Role.STUDENT,
            password="safe-test-password",
        ),
    }


def start_attempt(client, lesson):
    return client.post(reverse("lesson-attempt-start", kwargs={"slug": lesson.slug}))


def answer_payload(question, correct=True):
    if question.type == Question.Type.MCQ:
        choice = question.choices.filter(is_correct=correct).first()
        return {"questionId": question.id, "choiceId": choice.id}
    if question.type == Question.Type.ORDERING:
        words = question.answer_data["correct"].split()
        return {
            "questionId": question.id,
            "order": words if correct else list(reversed(words)),
        }
    return {
        "questionId": question.id,
        "answer": question.answer_data["correct"] if correct else "completely wrong",
    }


def answer_all(client, attempt_id, lesson, *, correct=True):
    endpoint = reverse("lesson-attempt-answer", kwargs={"attempt_id": attempt_id})
    responses = []
    for question in lesson.questions.prefetch_related("choices").all():
        responses.append(
            client.post(endpoint, answer_payload(question, correct=correct), format="json")
        )
    return responses


@pytest.fixture
def enrolled_student(published_course, users):
    Enrollment.objects.create(student=users["student"], course=published_course)
    lesson = published_course.units.first().lessons.first()
    return users["student"], lesson


@pytest.mark.django_db
def test_attempt_resumes_with_only_confirmed_feedback(enrolled_student):
    student, lesson = enrolled_student
    client = APIClient()
    client.force_login(student)

    started = start_attempt(client, lesson)
    question = lesson.questions.prefetch_related("choices").first()
    answered = client.post(
        reverse("lesson-attempt-answer", kwargs={"attempt_id": started.json()["id"]}),
        answer_payload(question),
        format="json",
    )
    resumed = start_attempt(client, lesson)

    assert started.status_code == answered.status_code == resumed.status_code == 200
    assert resumed.json()["id"] == started.json()["id"]
    assert resumed.json()["answeredCount"] == 1
    assert resumed.json()["answers"][0]["explanation"]
    assert LessonAttempt.objects.filter(status=LessonAttempt.Status.IN_PROGRESS).count() == 1


@pytest.mark.django_db
def test_identical_seed_preserves_questions_after_attempt_starts(enrolled_student):
    student, lesson = enrolled_student
    client = APIClient()
    client.force_login(student)
    start_attempt(client, lesson)
    question_ids = list(lesson.questions.values_list("id", flat=True))

    seed_curriculum()

    assert list(lesson.questions.values_list("id", flat=True)) == question_ids


@pytest.mark.django_db
def test_confirmed_answer_is_idempotent_but_cannot_be_changed(enrolled_student):
    student, lesson = enrolled_student
    client = APIClient()
    client.force_login(student)
    attempt_id = start_attempt(client, lesson).json()["id"]
    question = lesson.questions.filter(type=Question.Type.MCQ).prefetch_related("choices").first()
    endpoint = reverse("lesson-attempt-answer", kwargs={"attempt_id": attempt_id})
    correct = answer_payload(question)
    wrong = answer_payload(question, correct=False)

    first = client.post(endpoint, correct, format="json")
    repeated = client.post(endpoint, correct, format="json")
    changed = client.post(endpoint, wrong, format="json")

    assert first.status_code == repeated.status_code == 200
    assert first.json() == repeated.json()
    assert changed.status_code == 409
    assert changed.json()["code"] == "ANSWER_ALREADY_CONFIRMED"


@pytest.mark.django_db
def test_attempt_is_private_and_incomplete_finish_is_rejected(enrolled_student, users):
    student, lesson = enrolled_student
    owner = APIClient()
    owner.force_login(student)
    attempt_id = start_attempt(owner, lesson).json()["id"]
    finish_url = reverse("lesson-attempt-finish", kwargs={"attempt_id": attempt_id})

    incomplete = owner.post(finish_url)
    stranger = APIClient()
    stranger.force_login(users["other"])
    hidden = stranger.get(reverse("lesson-attempt-detail", kwargs={"attempt_id": attempt_id}))

    assert incomplete.status_code == 409
    assert incomplete.json()["code"] == "ATTEMPT_INCOMPLETE"
    assert hidden.status_code == 404


@pytest.mark.django_db
def test_first_pass_awards_xp_once_and_updates_outline_and_dashboard(enrolled_student):
    student, lesson = enrolled_student
    client = APIClient()
    client.force_login(student)
    attempt_id = start_attempt(client, lesson).json()["id"]
    assert all(response.status_code == 200 for response in answer_all(client, attempt_id, lesson))
    finish_url = reverse("lesson-attempt-finish", kwargs={"attempt_id": attempt_id})

    finished = client.post(finish_url)
    repeated = client.post(finish_url)
    dashboard = client.get(reverse("student-dashboard"))
    outline = client.get(
        reverse(
            "authorized-course-outline",
            kwargs={"slug": lesson.unit.course.slug},
        )
    )

    assert finished.status_code == repeated.status_code == 200
    assert finished.json() == repeated.json()
    assert finished.json()["passed"] is True
    assert finished.json()["xpAwarded"] == lesson.xp_reward
    assert XPEvent.objects.filter(student=student).count() == 1
    assert dashboard.json()["xp"] == lesson.xp_reward
    assert dashboard.json()["completedLessons"] == 1
    lesson_payload = next(
        item
        for unit in outline.json()["units"]
        for item in unit["lessons"]
        if item["slug"] == lesson.slug
    )
    assert lesson_payload["completed"] is True
    assert lesson_payload["bestScore"] == 100


@pytest.mark.django_db
def test_two_of_three_answers_pass_exact_sixty_six_percent_threshold(enrolled_student):
    student, lesson = enrolled_student
    removed = lesson.questions.filter(position__gt=3)
    Choice.objects.filter(question__in=removed).delete()
    removed.delete()
    lesson.passing_percent = 66
    lesson.save(update_fields=("passing_percent",))
    client = APIClient()
    client.force_login(student)
    attempt_id = start_attempt(client, lesson).json()["id"]
    endpoint = reverse("lesson-attempt-answer", kwargs={"attempt_id": attempt_id})

    for index, question in enumerate(
        lesson.questions.prefetch_related("choices").all()
    ):
        response = client.post(
            endpoint,
            answer_payload(question, correct=index < 2),
            format="json",
        )
        assert response.status_code == 200
    finished = client.post(
        reverse("lesson-attempt-finish", kwargs={"attempt_id": attempt_id})
    )

    assert finished.json()["correctCount"] == 2
    assert finished.json()["totalQuestions"] == 3
    assert finished.json()["scorePercent"] == 67
    assert finished.json()["passed"] is True


@pytest.mark.django_db
def test_failed_attempt_allows_retry_and_review_does_not_repeat_xp(enrolled_student):
    student, lesson = enrolled_student
    client = APIClient()
    client.force_login(student)

    failed_id = start_attempt(client, lesson).json()["id"]
    answer_all(client, failed_id, lesson, correct=False)
    failed = client.post(reverse("lesson-attempt-finish", kwargs={"attempt_id": failed_id}))

    passed_id = start_attempt(client, lesson).json()["id"]
    answer_all(client, passed_id, lesson)
    passed = client.post(reverse("lesson-attempt-finish", kwargs={"attempt_id": passed_id}))

    review_id = start_attempt(client, lesson).json()["id"]
    answer_all(client, review_id, lesson)
    review = client.post(reverse("lesson-attempt-finish", kwargs={"attempt_id": review_id}))

    assert failed.json()["passed"] is False
    assert failed.json()["xpAwarded"] == 0
    assert failed_id != passed_id != review_id
    assert passed.json()["xpAwarded"] == lesson.xp_reward
    assert review.json()["passed"] is True
    assert review.json()["xpAwarded"] == 0
    assert XPEvent.objects.filter(student=student).count() == 1
    progress = LessonProgress.objects.get(student=student, lesson=lesson)
    assert progress.completed is True
    assert progress.best_score == 100


@pytest.mark.django_db
def test_attempt_mutations_require_csrf(enrolled_student):
    student, lesson = enrolled_student
    client = APIClient(enforce_csrf_checks=True)
    csrf_token = client.get(reverse("accounts:csrf")).json()["csrfToken"]
    client.force_login(student)
    endpoint = reverse("lesson-attempt-start", kwargs={"slug": lesson.slug})

    denied = client.post(endpoint)
    allowed = client.post(endpoint, HTTP_X_CSRFTOKEN=csrf_token)

    assert denied.status_code == 403
    assert allowed.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_concurrent_finish_emits_one_xp_event(published_course, users):
    student = users["student"]
    lesson = published_course.units.first().lessons.first()
    Enrollment.objects.create(student=student, course=published_course)
    client = APIClient()
    client.force_login(student)
    attempt_id = start_attempt(client, lesson).json()["id"]
    answer_all(client, attempt_id, lesson)
    barrier = Barrier(2)

    def finish_in_thread():
        connections.close_all()
        try:
            thread_student = User.objects.get(id=student.id)
            barrier.wait()
            return finish_attempt(attempt_id=attempt_id, student=thread_student).xp_awarded
        finally:
            connections.close_all()

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(lambda _index: finish_in_thread(), range(2)))

    assert results == [lesson.xp_reward, lesson.xp_reward]
    assert XPEvent.objects.filter(student=student).count() == 1
