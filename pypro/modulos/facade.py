from django.shortcuts import get_object_or_404
from typing import List
from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista os módulos ordenados pela propriedade order
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def buscar_modulo(modulo_slug: str) -> Modulo:
    return get_object_or_404(Modulo, slug=modulo_slug)
