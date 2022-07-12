from django.test.client import Client
from model_bakery import baker
from pytest import fixture


@fixture
def usuario_logado(db, django_user_model):
    usuario_modelo = baker.make(django_user_model, _fill_optional=True)
    return usuario_modelo


@fixture
def client_usuario_logado(client: Client, usuario_logado):
    client.force_login(usuario_logado)
    return client
