from typing import List
from django.urls import reverse
from model_mommy import mommy
from pytest import fixture
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@fixture
def modulo(db):
    return mommy.make(Modulo)


@fixture
def aulas(modulo):
    return mommy.make(Aula, 3, modulo=modulo)


@fixture
def response(client, modulo: Modulo, aulas):
    resp = client.get(reverse("modulos:detalhe", args=(modulo.slug,)))
    return resp


def test_titulo(response, modulo: Modulo):
    assert_contains(response, modulo.titulo)


def test_publico(response, modulo: Modulo):
    assert_contains(response, modulo.publico)


def test_descricao(response, modulo: Modulo):
    assert_contains(response, modulo.descricao)


def test_aula_titulo(response, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(response, aula.titulo)


def test_aula_link(response, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(response, aula.get_absolute_url())
