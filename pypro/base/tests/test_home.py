from django.test import Client
from django.urls import reverse
from pytest import fixture
from pypro.django_assertions import assert_contains


@fixture
def response(client: Client):
    resp = client.get(reverse("base:home"))
    return resp


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, "<title>Python Pro - Home</title>")


def test_home_link(response):
    assert_contains(response, f'href="{reverse("base:home")}">Python Pro</a>')


def test_email_link(response):
    assert_contains(response, 'href="mailto:ramalho@python.pro.br"')
