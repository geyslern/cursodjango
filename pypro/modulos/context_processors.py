from django.http import HttpRequest
from pypro.modulos import facade


def listar_modulos(request: HttpRequest):
    return {"MODULOS": facade.listar_modulos_ordenados()}
