from pytest import fixture
from model_mommy import mommy
from pypro.modulos import facade
from pypro.modulos.models import Modulo


@fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in "Depois Antes".split()]


def test_listar_modulos_ordenados(modulos):
    db_modulos = facade.listar_modulos_ordenados()
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == db_modulos
