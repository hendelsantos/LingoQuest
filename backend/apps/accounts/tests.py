import re
from datetime import timedelta

import pytest
from django.core import mail
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from .models import Invitation, StudentProfile, TeacherProfile, User

PASSWORD = "correct-horse-battery-staple"


def csrf_client() -> tuple[APIClient, str]:
    client = APIClient(enforce_csrf_checks=True)
    response = client.get(reverse("accounts:csrf"))
    return client, response.json()["csrfToken"]


def invite_user(*, admin: User, role: str = User.Role.STUDENT):
    client, csrf_token = csrf_client()
    client.force_login(admin)
    response = client.post(
        reverse("accounts:invitation-create"),
        {"email": "new.user@example.com", "role": role},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )
    assert response.status_code == 201
    match = re.search(r"token=([^\s]+)", mail.outbox[-1].body)
    assert match is not None
    return client, match.group(1)


@pytest.mark.django_db
def test_user_email_is_normalized_to_lowercase():
    user = User.objects.create_user(
        email="Student@Example.COM", name="Student", password="safe-test-password"
    )

    assert user.email == "student@example.com"
    assert user.role == User.Role.STUDENT


@pytest.mark.django_db
def test_login_creates_session_and_me_returns_server_role():
    user = User.objects.create_user(
        email="student@example.com",
        name="Student",
        role=User.Role.STUDENT,
        password=PASSWORD,
    )
    client, csrf_token = csrf_client()

    response = client.post(
        reverse("accounts:login"),
        {
            "email": user.email,
            "password": PASSWORD,
            "role": User.Role.ADMIN,
        },
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )

    assert response.status_code == 200
    assert response.json()["user"]["role"] == User.Role.STUDENT
    me = client.get(reverse("accounts:me"))
    assert me.status_code == 200
    assert me.json()["id"] == str(user.id)


@pytest.mark.django_db
def test_public_authentication_posts_require_csrf():
    user = User.objects.create_user(
        email="student@example.com", name="Student", password=PASSWORD
    )
    client = APIClient(enforce_csrf_checks=True)

    response = client.post(
        reverse("accounts:login"),
        {"email": user.email, "password": PASSWORD},
        format="json",
    )

    assert response.status_code == 403


@pytest.mark.django_db
def test_logout_invalidates_session_and_requires_csrf():
    user = User.objects.create_user(
        email="student@example.com", name="Student", password=PASSWORD
    )
    client, csrf_token = csrf_client()
    client.force_login(user)

    denied = client.post(reverse("accounts:logout"), format="json")
    response = client.post(
        reverse("accounts:logout"),
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )

    assert denied.status_code == 403
    assert response.status_code == 200
    assert client.get(reverse("accounts:me")).status_code == 403


@pytest.mark.django_db
def test_inactive_user_cannot_login_or_keep_existing_session():
    user = User.objects.create_user(
        email="student@example.com", name="Student", password=PASSWORD
    )
    client, csrf_token = csrf_client()
    client.force_login(user)
    user.is_active = False
    user.save(update_fields=("is_active",))

    assert client.get(reverse("accounts:me")).status_code == 403
    login_response = client.post(
        reverse("accounts:login"),
        {"email": user.email, "password": PASSWORD},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )
    assert login_response.status_code == 400


@pytest.mark.django_db
def test_only_admin_role_can_create_invitation():
    student = User.objects.create_user(
        email="student@example.com", name="Student", password=PASSWORD
    )
    client, csrf_token = csrf_client()
    client.force_login(student)

    response = client.post(
        reverse("accounts:invitation-create"),
        {"email": "other@example.com", "role": User.Role.TEACHER},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )

    assert response.status_code == 403
    assert Invitation.objects.count() == 0


@pytest.mark.django_db
@pytest.mark.parametrize(
    ("role", "profile_model"),
    [
        (User.Role.STUDENT, StudentProfile),
        (User.Role.TEACHER, TeacherProfile),
    ],
)
def test_invitation_is_hashed_single_use_and_creates_role_profile(role, profile_model):
    admin = User.objects.create_user(
        email="admin@example.com",
        name="Admin",
        role=User.Role.ADMIN,
        password=PASSWORD,
    )
    _, raw_token = invite_user(admin=admin, role=role)
    invitation = Invitation.objects.get()
    assert raw_token not in invitation.token_hash

    client, csrf_token = csrf_client()
    response = client.post(
        reverse("accounts:invitation-accept"),
        {"token": raw_token, "name": "New User", "password": PASSWORD},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )

    assert response.status_code == 201
    user = User.objects.get(email="new.user@example.com")
    assert user.role == role
    assert profile_model.objects.filter(user=user).exists()
    assert client.get(reverse("accounts:me")).status_code == 200
    invitation.refresh_from_db()
    assert invitation.used_at is not None

    second_client, second_csrf = csrf_client()
    reused = second_client.post(
        reverse("accounts:invitation-accept"),
        {"token": raw_token, "name": "Other", "password": PASSWORD},
        format="json",
        HTTP_X_CSRFTOKEN=second_csrf,
    )
    assert reused.status_code == 400


@pytest.mark.django_db
def test_expired_invitation_is_rejected():
    admin = User.objects.create_user(
        email="admin@example.com",
        name="Admin",
        role=User.Role.ADMIN,
        password=PASSWORD,
    )
    _, raw_token = invite_user(admin=admin)
    Invitation.objects.update(expires_at=timezone.now() - timedelta(seconds=1))
    client, csrf_token = csrf_client()

    response = client.post(
        reverse("accounts:invitation-accept"),
        {"token": raw_token, "name": "New User", "password": PASSWORD},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )

    assert response.status_code == 400
    assert not User.objects.filter(email="new.user@example.com").exists()


@pytest.mark.django_db
def test_password_reset_request_does_not_enumerate_accounts_and_token_is_single_use():
    user = User.objects.create_user(
        email="student@example.com", name="Student", password=PASSWORD
    )
    client, csrf_token = csrf_client()
    endpoint = reverse("accounts:password-reset")

    missing = client.post(
        endpoint,
        {"email": "missing@example.com"},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )
    existing = client.post(
        endpoint,
        {"email": user.email},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )

    assert missing.status_code == existing.status_code == 200
    assert missing.json() == existing.json()
    assert len(mail.outbox) == 1
    match = re.search(r"uid=([^&]+)&token=([^\s]+)", mail.outbox[0].body)
    assert match is not None
    uid, token = match.groups()
    new_password = "another-correct-horse-battery-staple"
    confirmed = client.post(
        reverse("accounts:password-reset-confirm"),
        {"uid": uid, "token": token, "password": new_password},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )
    reused = client.post(
        reverse("accounts:password-reset-confirm"),
        {"uid": uid, "token": token, "password": PASSWORD},
        format="json",
        HTTP_X_CSRFTOKEN=csrf_token,
    )
    user.refresh_from_db()

    assert confirmed.status_code == 200
    assert reused.status_code == 400
    assert user.check_password(new_password)

