from django.shortcuts import render
from pypro.modulos import facade


def detalhe(request, modulo_slug):
    modulo = facade.buscar_modulo(modulo_slug)
    aulas = facade.listar_aulas_do_modulo_ordenadas(modulo)
    return render(request, "modulos/detalhe.html", context={"modulo": modulo, "aulas": aulas})


def aula(request, aula_slug):
    aula = facade.buscar_aula(aula_slug)
    return render(request, "modulos/aula_detalhe.html", context={"aula": aula})
