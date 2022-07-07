from typing import List
from pypro.turmas.models import Turma


def listar_turmas() -> List[Turma]:
    return Turma.objects.all()
