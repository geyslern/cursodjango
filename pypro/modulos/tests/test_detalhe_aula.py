from django.http import HttpResponse
from django.urls import reverse
from model_bakery import baker
from pytest import fixture
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@fixture
def modulo(db):
    return baker.make(Modulo)


@fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@fixture
def response_com_usuario(client_usuario_logado, aula: Aula):
    resp = client_usuario_logado.get(reverse("modulos:aula", args=(aula.slug,)))
    return resp


@fixture
def response_sem_usuario(client, aula: Aula):
    resp = client.get(reverse("modulos:aula", args=(aula.slug,)))
    return resp


def test_titulo(response_com_usuario, aula: Aula):
    assert_contains(response_com_usuario, aula.titulo)


def test_vimeo(response_com_usuario, aula: Aula):
    assert_contains(response_com_usuario, f"https://player.vimeo.com/video/{aula.vimeo_id}")


def test_modulo_breadcrumb(response_com_usuario, modulo: Modulo):
    assert_contains(
        response_com_usuario,
        f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>'
    )


def test_usuario_nao_logado_redirect(response_sem_usuario: HttpResponse):
    assert response_sem_usuario.status_code == 302
    assert response_sem_usuario.url.startswith(reverse("login"))
