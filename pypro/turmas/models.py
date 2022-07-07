from django.db import models
from django.contrib.auth import get_user_model


class Turma(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()
    fim = models.DateField()
    alunos = models.ManyToManyField(get_user_model(), through="Matricula")

    def __str__(self) -> str:
        return f"{self.nome}"


class Matricula(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["usuario", "turma"], name="matricula_unica")
        ]
        ordering = ["turma", "data"]

    def __str__(self) -> str:
        return f"Matrícula de {self.usuario.first_name} na turma {self.turma}"
