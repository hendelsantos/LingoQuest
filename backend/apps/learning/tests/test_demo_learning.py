import pytest
from django.core.management import call_command
from django.urls import reverse
from rest_framework.test import APIClient

from apps.learning.models import Course, Lesson


@pytest.fixture
def seeded_course():
    call_command("seed_demo", verbosity=0)
    return Course.objects.get(slug="a1-foundations")


@pytest.mark.django_db
def test_seed_is_idempotent():
    call_command("seed_demo", verbosity=0)
    call_command("seed_demo", verbosity=0)

    assert Course.objects.count() == 1
    assert Lesson.objects.count() == 8
    assert sum(lesson.questions.count() for lesson in Lesson.objects.all()) == 24


@pytest.mark.django_db
def test_lesson_payload_never_leaks_answer(seeded_course):
    response = APIClient().get(reverse("demo-lesson-detail", kwargs={"slug": "tobe"}))

    assert response.status_code == 200
    payload = response.json()
    assert len(payload["questions"]) == 3
    assert "is_correct" not in str(payload).lower()
    assert "correctChoiceId" not in payload["questions"][0]
    assert "explanation" not in payload["questions"][0]


@pytest.mark.django_db
def test_answer_is_checked_on_server(seeded_course):
    lesson = Lesson.objects.prefetch_related("questions__choices").get(slug="tobe")
    question = lesson.questions.first()
    correct_choice = question.choices.get(is_correct=True)

    response = APIClient().post(
        reverse("demo-answer", kwargs={"slug": lesson.slug}),
        {"questionId": question.id, "choiceId": correct_choice.id},
        format="json",
    )

    assert response.status_code == 200
    assert response.json()["isCorrect"] is True
    assert response.json()["correctChoiceId"] == correct_choice.id
    assert response.json()["explanation"]
