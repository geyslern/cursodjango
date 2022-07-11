from django.http import HttpResponse
from django.test.client import Client
from django.urls import reverse
from model_bakery import baker
from pytest import fixture
from pypro.base.models import User


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


def test_login_form_page(response: HttpResponse):
    assert response.status_code == 200


def test_login_redirect(response_post: HttpResponse):
    assert response_post.status_code == 302
    assert response_post.url == reverse("modulos:indice")
