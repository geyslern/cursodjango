from django.http import HttpResponse
from django.urls import reverse
from model_bakery import baker
from pytest import fixture
from pypro.django_assertions import assert_contains
from pypro.turmas.models import Turma
from typing import List


@fixture
def turmas(db):
    return baker.make(Turma, 3)


@fixture
def response(client, turmas):
    resp = client.get(reverse("turmas:indice"))
    return resp


def test_indice_disponivel(response: HttpResponse):
    assert response.status_code == 200


def test_turmas_nome(response: HttpResponse, turmas: List[Turma]):
    for turma in turmas:
        assert_contains(response, turma.nome)
