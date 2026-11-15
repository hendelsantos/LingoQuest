import pytest

from .models import User


@pytest.mark.django_db
def test_user_email_is_normalized_to_lowercase():
    user = User.objects.create_user(
        email="Student@Example.COM", name="Student", password="safe-test-password"
    )

    assert user.email == "student@example.com"
    assert user.role == User.Role.STUDENT

