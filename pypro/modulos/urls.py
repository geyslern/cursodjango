from django.urls import path
from pypro.modulos import views


app_name = "modulos"
urlpatterns = [
    path("", views.indice, name="indice"),
    path("<slug:modulo_slug>", views.detalhe, name="detalhe"),
    path("aulas/<slug:aula_slug>", views.aula, name="aula")
]
