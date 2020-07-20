from django.test import Client
from plataforma.django_assertions import assert_contains


def test_status_code(client: Client):
    resp = client.get('/')
    assert 200 == resp.status_code


def test_title(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Curso Plataforma Django</title>')
