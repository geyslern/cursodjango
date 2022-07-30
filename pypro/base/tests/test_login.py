from django.http import HttpResponse
from django.test.client import Client
from django.urls import reverse
from django.utils.translation import gettext as _
from model_bakery import baker
from pytest import fixture
from pypro.django_assertions import assert_contains, assert_not_contains


@fixture
def usuario(db, django_user_model):
    passwd = "senha plana"
    usuario_modelo = baker.make(django_user_model)
    usuario_modelo.set_password(passwd)
    usuario_modelo.senha_plana = passwd
    usuario_modelo.save()
    return usuario_modelo


@fixture
def response(client, db):
    return client.get(reverse("login"))


@fixture
def response_post(client: Client, usuario):
    resp = client.post(reverse("login"), data={"username": usuario.email, "password": usuario.senha_plana},)
    return resp


@fixture
def response_home(client, db):
    resp = client.get(reverse("base:home"))
    return resp


@fixture
def response_home_usuario_logado(client_usuario_logado, db):
    resp = client_usuario_logado.get(reverse("base:home"))
    return resp


def test_login_form_page(response: HttpResponse):
    assert response.status_code == 200


def test_login_redirect(response_post: HttpResponse):
    assert response_post.status_code == 302
    assert response_post.url == reverse("modulos:indice")


def test_botao_login_disponivel(response_home: HttpResponse):
    assert_contains(response_home, _("Log in"))


def test_link_login_disponivel(response_home: HttpResponse):
    assert_contains(response_home, reverse("login"))


def test_botao_login_indisponivel(response_home_usuario_logado: HttpResponse):
    assert_not_contains(response_home_usuario_logado, "Entrar")


def test_link_login_indisponivel(response_home_usuario_logado: HttpResponse):
    assert_not_contains(response_home_usuario_logado, reverse("login"))


def test_botao_sair_disponivel(response_home_usuario_logado: HttpResponse):
    assert_contains(response_home_usuario_logado, _("Log out"))


def test_nome_usuario_logado_disponivel(response_home_usuario_logado: HttpResponse, usuario_logado):
    assert_contains(response_home_usuario_logado, usuario_logado.first_name)


def test_link_sair_disponivel(response_home_usuario_logado: HttpResponse):
    assert_contains(response_home_usuario_logado, reverse("logout"))
