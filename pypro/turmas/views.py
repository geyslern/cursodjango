from django.shortcuts import render
from pypro.turmas import facade


def indice(request):
    turmas = facade.listar_turmas()
    return render(request, "turmas/indice.html", context={"turmas": turmas})
