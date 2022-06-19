from django.shortcuts import render
from pypro.modulos import facade


def detalhe(request, modulo_slug):
    modulo = facade.buscar_modulo(modulo_slug)
    return render(request, "modulos/detalhe.html", context={"modulo": modulo})
