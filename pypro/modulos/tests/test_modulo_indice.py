from typing import List
from django.urls import reverse
from django.http import HttpResponse
from model_bakery import baker
from pytest import fixture
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@fixture
def modulos(db):
    return baker.make(Modulo, 3)


@fixture
def aulas(modulos: Modulo):
    aulas = []
    for modulo in modulos:
        aulas.extend(baker.make(Aula, 3, modulo=modulo))

    return aulas


@fixture
def response(client, modulos: List[Modulo], aulas: List[Aula]):
    resp = client.get(reverse("modulos:indice"))
    return resp


def test_indice_disponivel(response: HttpResponse):
    assert response.status_code == 200


def test_titulo(response, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(response, modulo.titulo)


def test_publico(response, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(response, modulo.publico)


def test_descricao(response, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(response, modulo.descricao)


def test_aula_titulo(response, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(response, aula.titulo)


def test_aula_link(response, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(response, aula.get_absolute_url())
