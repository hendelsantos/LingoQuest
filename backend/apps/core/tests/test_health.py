import pytest
from django.test import override_settings
from django.urls import reverse


@pytest.mark.django_db
def test_health_endpoint_is_public(client):
    response = client.get(reverse("health"))

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "lingoquest-api"}


@pytest.mark.django_db
@override_settings(SECURE_SSL_REDIRECT=True, SECURE_REDIRECT_EXEMPT=[r"^health/$"])
def test_health_endpoint_is_not_redirected_by_https_enforcement(client):
    response = client.get(reverse("health"))

    assert response.status_code == 200

