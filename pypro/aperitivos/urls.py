from django.urls import path
from pypro.aperitivos.views import indice, video


app_name = "aperitivos"
urlpatterns = [
    path("", indice, name="indice"),
    path("<slug:slug>", video, name="video"),
]
