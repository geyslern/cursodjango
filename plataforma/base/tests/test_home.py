import pytest
from plataforma.django_assertions import assert_contains
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert 200 == resp.status_code


def test_title(resp):
    assert_contains(resp, '<title>Curso Plataforma Django</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{ reverse("base:home") }">Python Pro</a>')
