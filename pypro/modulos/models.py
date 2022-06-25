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


class Aula(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    modulo = models.ForeignKey("Modulo", on_delete=models.PROTECT)
    order_with_respect_to = "modulo"
    vimeo_id = models.CharField(max_length=32)

    class Meta:
        ordering = ("modulo", "order")

    def __str__(self) -> str:
        return self.titulo

    def get_absolute_url(self) -> str:
        return reverse("modulos:aula", args=(self.slug,))
