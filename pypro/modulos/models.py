from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    descricao = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self) -> str:
        return reverse("modulos:detalhe", args=(self.slug,))
