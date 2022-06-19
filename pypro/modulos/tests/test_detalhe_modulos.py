from django.urls import reverse
from model_mommy import mommy
from pytest import fixture
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo


@fixture
def modulo(db):
    return mommy.make(Modulo)


@fixture
def response(client, modulo):
    resp = client.get(reverse("modulos:detalhe", args=(modulo.slug,)))
    return resp


def test_titulo(response, modulo: Modulo):
    assert_contains(response, modulo.titulo)


def test_publico(response, modulo: Modulo):
    assert_contains(response, modulo.publico)


def test_descricao(response, modulo: Modulo):
    assert_contains(response, modulo.descricao)
