from typing import List
from pytest import fixture
from model_mommy import mommy
from pypro.modulos import facade
from pypro.modulos.models import Modulo


@fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in "Depois Antes".split()]


def test_listar_modulos_ordenados(modulos: List[Modulo]):
    db_modulos = facade.listar_modulos_ordenados()
    assert list(sorted(modulos, key=lambda modulo: modulo.order)) == db_modulos


def test_buscar_modulo(modulos: List[Modulo]):
    for modulo in modulos:
        assert modulo == facade.buscar_modulo(modulo.slug)
