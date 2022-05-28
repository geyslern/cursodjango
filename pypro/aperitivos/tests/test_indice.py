import pytest
from django.urls import reverse
from django.test import Client
from pypro.django_assertions import assert_contains


@pytest.fixture
def response_indice(client: Client):
    return client.get(reverse("aperitivos:indice"))


def test_status_code(response_indice):
    assert response_indice.status_code == 200


def test_titulo_indice(response_indice):
    assert_contains(response_indice, "Vídeos Aperitivos")


@pytest.mark.parametrize("titulo", ["Video Aperitivo: Motivação", "Video Aperitivo: Instalação no Windows"])
def test_titulos_videos(response_indice, titulo):
    assert_contains(response_indice, titulo)


@pytest.mark.parametrize("slug", ["motivacao", "instalacao-windows"])
def test_link_motivacao(response_indice, slug):
    assert_contains(response_indice, f'href="{reverse("aperitivos:video", args=(slug,))}"')
