from django.urls import reverse
from model_bakery import baker
from pytest import fixture
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@fixture
def modulo(db):
    return baker.make(Modulo)


@fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@fixture
def response(client, aula: Aula):
    resp = client.get(reverse("modulos:aula", args=(aula.slug,)))
    return resp


def test_titulo(response, aula: Aula):
    assert_contains(response, aula.titulo)


def test_vimeo(response, aula: Aula):
    assert_contains(response, f"https://player.vimeo.com/video/{aula.vimeo_id}")


def test_modulo_breadcrumb(response, modulo: Modulo):
    assert_contains(response, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')
