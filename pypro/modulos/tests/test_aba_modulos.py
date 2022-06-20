from django.urls import reverse
from model_mommy import mommy
from pytest import fixture
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo


@fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@fixture
def response(client, modulos):
    resp = client.get(reverse("base:home"))
    return resp


def test_titulos_dos_modulos(response, modulos):
    for modulo in modulos:
        assert_contains(response, modulo.titulo)


def test_link_dos_modulos(response, modulos):
    for modulo in modulos:
        assert_contains(response, modulo.get_absolute_url())
