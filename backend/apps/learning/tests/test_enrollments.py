import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from apps.accounts.models import User
from apps.learning.models import Course, Enrollment
from apps.learning.services import seed_curriculum


@pytest.fixture
def published_course(db):
    seed_curriculum()
    return Course.objects.get(slug="a1-foundations")


@pytest.fixture
def users(db):
    return {
        "admin": User.objects.create_user(
            email="admin@example.com",
            name="Admin",
            role=User.Role.ADMIN,
            password="safe-test-password",
        ),
        "student": User.objects.create_user(
            email="student@example.com",
            name="Student",
            role=User.Role.STUDENT,
            password="safe-test-password",
        ),
        "other": User.objects.create_user(
            email="other@example.com",
            name="Other Student",
            role=User.Role.STUDENT,
            password="safe-test-password",
        ),
        "teacher": User.objects.create_user(
            email="teacher@example.com",
            name="Teacher",
            role=User.Role.TEACHER,
            password="safe-test-password",
        ),
    }


def authenticated_client(user):
    client = APIClient()
    client.force_login(user)
    return client


@pytest.mark.django_db
def test_admin_creates_enrollment_and_duplicate_is_rejected(published_course, users):
    client = authenticated_client(users["admin"])
    payload = {"studentId": users["student"].id, "courseSlug": published_course.slug}

    created = client.post(reverse("admin-enrollments"), payload, format="json")
    duplicate = client.post(reverse("admin-enrollments"), payload, format="json")

    assert created.status_code == 201
    assert created.json()["student"]["email"] == "student@example.com"
    assert created.json()["course"]["slug"] == "a1-foundations"
    assert created.json()["status"] == Enrollment.Status.ACTIVE
    assert duplicate.status_code == 400
    assert Enrollment.objects.count() == 1


@pytest.mark.django_db
def test_only_admin_can_manage_enrollments(published_course, users):
    client = authenticated_client(users["student"])

    response = client.post(
        reverse("admin-enrollments"),
        {"studentId": users["student"].id, "courseSlug": published_course.slug},
        format="json",
    )

    assert response.status_code == 403
    assert not Enrollment.objects.exists()


@pytest.mark.django_db
def test_admin_enrollment_mutation_requires_csrf(published_course, users):
    client = APIClient(enforce_csrf_checks=True)
    csrf_token = client.get(reverse("accounts:csrf")).json()["csrfToken"]
    client.force_login(users["admin"])
    payload = {"studentId": users["student"].id, "courseSlug": published_course.slug}

    denied = client.post(reverse("admin-enrollments"), payload, format="json")
    allowed = client.post(
        reverse("admin-enrollments"),
        payload,
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )

    assert denied.status_code == 403
    assert allowed.status_code == 201


@pytest.mark.django_db
def test_student_lists_only_own_enrollments_including_inactive_statuses(
    published_course, users
):
    own = Enrollment.objects.create(
        student=users["student"],
        course=published_course,
        status=Enrollment.Status.PAUSED,
    )
    other_course = Course.objects.get(slug="a2-everyday-english")
    Enrollment.objects.create(student=users["other"], course=other_course)

    response = authenticated_client(users["student"]).get(reverse("student-enrollments"))

    assert response.status_code == 200
    assert [item["id"] for item in response.json()] == [str(own.id)]
    assert response.json()[0]["status"] == Enrollment.Status.PAUSED


@pytest.mark.django_db
def test_active_student_reads_only_enrolled_published_course_without_answers(
    published_course, users
):
    Enrollment.objects.create(student=users["student"], course=published_course)
    client = authenticated_client(users["student"])

    outline = client.get(
        reverse("authorized-course-outline", kwargs={"slug": published_course.slug})
    )
    lesson = client.get(reverse("authorized-lesson-detail", kwargs={"slug": "hello"}))
    unrelated = client.get(
        reverse("authorized-course-outline", kwargs={"slug": "a2-everyday-english"})
    )

    assert outline.status_code == 200
    assert outline.json()["slug"] == published_course.slug
    assert lesson.status_code == 200
    assert "is_correct" not in str(lesson.json()).lower()
    assert "answer_data" not in str(lesson.json()).lower()
    assert unrelated.status_code == 404


@pytest.mark.django_db
def test_attempt_start_requires_enrollment(published_course, users):
    Enrollment.objects.create(student=users["student"], course=published_course)
    lesson = published_course.units.first().lessons.first()

    allowed = authenticated_client(users["student"]).post(
        reverse("lesson-attempt-start", kwargs={"slug": lesson.slug}),
    )
    denied = authenticated_client(users["other"]).post(
        reverse("lesson-attempt-start", kwargs={"slug": lesson.slug}),
    )

    assert allowed.status_code == 200
    assert denied.status_code == 404


@pytest.mark.django_db
def test_paused_or_cancelled_enrollment_blocks_course_and_lesson(published_course, users):
    enrollment = Enrollment.objects.create(
        student=users["student"],
        course=published_course,
        status=Enrollment.Status.PAUSED,
    )
    client = authenticated_client(users["student"])

    assert client.get(
        reverse("authorized-course-outline", kwargs={"slug": published_course.slug})
    ).status_code == 404
    assert client.get(
        reverse("authorized-lesson-detail", kwargs={"slug": "hello"})
    ).status_code == 404

    enrollment.status = Enrollment.Status.COMPLETED
    enrollment.save(update_fields=("status",))
    assert client.get(
        reverse("authorized-course-outline", kwargs={"slug": published_course.slug})
    ).status_code == 200


@pytest.mark.django_db
def test_admin_status_change_tracks_end_and_reactivation(published_course, users):
    enrollment = Enrollment.objects.create(student=users["student"], course=published_course)
    client = authenticated_client(users["admin"])
    endpoint = reverse("admin-enrollment-detail", kwargs={"enrollment_id": enrollment.id})

    cancelled = client.patch(endpoint, {"status": "CANCELLED"}, format="json")
    reactivated = client.patch(endpoint, {"status": "ACTIVE"}, format="json")

    assert cancelled.status_code == 200
    assert cancelled.json()["endedAt"] is not None
    assert reactivated.status_code == 200
    assert reactivated.json()["endedAt"] is None


@pytest.mark.django_db
def test_teacher_cannot_use_student_curriculum_endpoints(published_course, users):
    response = authenticated_client(users["teacher"]).get(
        reverse("authorized-course-outline", kwargs={"slug": published_course.slug})
    )

    assert response.status_code == 403
