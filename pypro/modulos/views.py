from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from pypro.modulos import facade


def indice(request):
    modulos = facade.listar_modulos_com_aulas()
    return render(request, "modulos/indice.html", context={"modulos": modulos})


def detalhe(request, modulo_slug):
    modulo = facade.buscar_modulo(modulo_slug)
    aulas = facade.listar_aulas_do_modulo_ordenadas(modulo)
    return render(request, "modulos/detalhe.html", context={"modulo": modulo, "aulas": aulas})


@login_required
def aula(request, aula_slug):
    aula = facade.buscar_aula(aula_slug)
    return render(request, "modulos/aula_detalhe.html", context={"aula": aula})
