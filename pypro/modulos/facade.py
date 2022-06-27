from django.shortcuts import get_object_or_404
from django.db.models.query import Prefetch
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
    return Aula.objects.select_related("modulo").get(slug=aula_slug)


def listar_modulos_com_aulas():
    aulas_ordenadas = Aula.objects.order_by("order").all()
    return Modulo.objects.order_by("order").prefetch_related(
        Prefetch("aula_set", queryset=aulas_ordenadas, to_attr="aulas")
    ).all()
