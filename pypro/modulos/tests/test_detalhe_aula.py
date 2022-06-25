from django.urls import reverse
from model_mommy import mommy
from pytest import fixture
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@fixture
def modulo(db):
    return mommy.make(Modulo)


@fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@fixture
def response(client, aula: Aula):
    resp = client.get(reverse("modulos:aula", args=(aula.slug,)))
    return resp


def test_titulo(response, aula: Aula):
    assert_contains(response, aula.titulo)


def test_vimeo(response, aula: Aula):
    assert_contains(response, f"https://player.vimeo.com/video/{aula.vimeo_id}")
