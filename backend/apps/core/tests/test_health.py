import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_health_endpoint_is_public(client):
    response = client.get(reverse("health"))

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "lingoquest-api"}

