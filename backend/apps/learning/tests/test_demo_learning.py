import pytest
from django.core.management import call_command
from django.urls import reverse
from rest_framework.test import APIClient

from apps.learning.content import load_catalog
from apps.learning.models import Choice, Course, Lesson, Question


def catalog_totals():
    courses = units = lessons = questions = 0
    for _course_data, units_data in load_catalog():
        courses += 1
        units += len(units_data)
        for unit_data in units_data:
            lessons += len(unit_data["lessons"])
            questions += sum(len(lesson["questions"]) for lesson in unit_data["lessons"])
    return {"courses": courses, "units": units, "lessons": lessons, "questions": questions}



@pytest.fixture
def seeded_course():
    call_command("seed_demo", verbosity=0)
    return Course.objects.get(slug="a1-foundations")


@pytest.mark.django_db
def test_seed_is_idempotent():
    expected = catalog_totals()
    call_command("seed_demo", verbosity=0)
    call_command("seed_demo", verbosity=0)

    assert Course.objects.count() == expected["courses"]
    assert Lesson.objects.count() == expected["lessons"]
    assert sum(lesson.questions.count() for lesson in Lesson.objects.all()) == expected["questions"]
    # Slugs de lição precisam ser globalmente únicos (a busca é por slug).
    slugs = list(Lesson.objects.values_list("slug", flat=True))
    assert len(slugs) == len(set(slugs))


@pytest.mark.django_db
def test_seed_removes_stale_lessons(seeded_course):
    lesson = Lesson.objects.get(slug="numbers")
    Choice.objects.filter(question__lesson=lesson).delete()
    lesson.questions.all().delete()
    lesson.delete()

    call_command("seed_demo", verbosity=0)

    assert Lesson.objects.filter(slug="numbers").exists()
    assert lesson_questions_count("numbers") == 5


@pytest.mark.django_db
def test_lesson_payload_never_leaks_answer(seeded_course):
    response = APIClient().get(reverse("demo-lesson-detail", kwargs={"slug": "tobe"}))

    assert response.status_code == 200
    payload = response.json()
    serialized = str(payload).lower()
    assert "is_correct" not in serialized
    assert "answerdata" not in serialized
    assert "accepted" not in serialized
    assert "correctanswer" not in serialized
    assert "explanation" not in payload["questions"][0]


def lesson_questions_count(slug: str) -> int:
    return Question.objects.filter(lesson__slug=slug).count()


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


@pytest.mark.django_db
def test_mcq_rejects_choice_from_another_question(seeded_course):
    question = Question.objects.filter(lesson__slug="tobe", type=Question.Type.MCQ).first()
    foreign_choice = Choice.objects.exclude(question=question).first()

    response = APIClient().post(
        reverse("demo-answer", kwargs={"slug": "tobe"}),
        {"questionId": question.id, "choiceId": foreign_choice.id},
        format="json",
    )

    assert response.status_code == 400
    assert response.json()["code"] == "CHOICE_NOT_AVAILABLE"


@pytest.mark.django_db
def test_fill_in_answer_accepts_equivalent_forms(seeded_course):
    question = Question.objects.get(lesson__slug="food-and-drinks", prompt__contains="fish")

    for answer in ("don't", "Do Not"):
        response = APIClient().post(
            reverse("demo-answer", kwargs={"slug": "food-and-drinks"}),
            {"questionId": question.id, "answer": answer},
            format="json",
        )
        assert response.status_code == 200, answer
        assert response.json()["isCorrect"] is True, answer

    response = APIClient().post(
        reverse("demo-answer", kwargs={"slug": "food-and-drinks"}),
        {"questionId": question.id, "answer": "doesn't"},
        format="json",
    )
    assert response.json()["isCorrect"] is False
    assert response.json()["correctAnswer"] == "don't"


@pytest.mark.django_db
def test_ordering_answer_checked_on_server(seeded_course):
    question = Question.objects.get(lesson__slug="tobe", type=Question.Type.ORDERING)

    correct_response = APIClient().post(
        reverse("demo-answer", kwargs={"slug": "tobe"}),
        {"questionId": question.id, "order": ["We", "are", "friends."]},
        format="json",
    )
    assert correct_response.json()["isCorrect"] is True

    wrong_response = APIClient().post(
        reverse("demo-answer", kwargs={"slug": "tobe"}),
        {"questionId": question.id, "order": ["Are", "we", "friends."]},
        format="json",
    )
    assert wrong_response.json()["isCorrect"] is False
    assert wrong_response.json()["correctAnswer"] == "We are friends."


@pytest.mark.django_db
def test_listening_answer_tolerates_small_typos(seeded_course):
    question = Question.objects.get(lesson__slug="there-is-are", type=Question.Type.LISTENING)

    response = APIClient().post(
        reverse("demo-answer", kwargs={"slug": "there-is-are"}),
        {"questionId": question.id, "answer": "There is a big park near my hous"},
        format="json",
    )
    assert response.status_code == 200
    assert response.json()["isCorrect"] is True

    empty_response = APIClient().post(
        reverse("demo-answer", kwargs={"slug": "there-is-are"}),
        {"questionId": question.id, "answer": ""},
        format="json",
    )
    assert empty_response.status_code == 400


@pytest.mark.django_db
def test_courses_list_endpoint(seeded_course):
    response = APIClient().get(reverse("demo-courses"))

    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == catalog_totals()["courses"]
    a1 = next(course for course in courses if course["slug"] == "a1-foundations")
    assert a1["level"] == "A1"
    assert a1["lessonCount"] == 20
    assert a1["unitCount"] == 5


@pytest.mark.django_db
def test_lesson_detail_includes_dialogue_and_types(seeded_course):
    response = APIClient().get(reverse("demo-lesson-detail", kwargs={"slug": "small-talk"}))

    payload = response.json()
    assert payload["dialogue"][0]["speaker"] == "Anna"
    assert "line" in payload["dialogue"][0]
    types = {question["type"] for question in payload["questions"]}
    assert "MCQ" in types
    assert "LISTENING" in types
    ordering = next(q for q in payload["questions"] if q["type"] == "ORDERING")
    assert sorted(ordering["tokens"]) == sorted(["How", "is", "it", "going"])
