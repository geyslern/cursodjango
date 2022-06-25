from django.shortcuts import get_object_or_404
from typing import List
from pypro.modulos.models import Aula, Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista os módulos ordenados pela propriedade order
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def buscar_modulo(modulo_slug: str) -> Modulo:
    return get_object_or_404(Modulo, slug=modulo_slug)


def listar_aulas_do_modulo_ordenadas(modulo: Modulo) -> List[Aula]:
    return list(modulo.aula_set.order_by("order").all())


def buscar_aula(aula_slug: str) -> Aula:
    return get_object_or_404(Aula, slug=aula_slug)
