import pytest
from django.urls import reverse
from django.test import Client
from pypro.django_assertions import assert_contains


@pytest.fixture
def response_motivacao(client: Client):
    return client.get(reverse("aperitivos:video", args=("motivacao",)))


@pytest.fixture
def response_instalacao(client: Client):
    return client.get(reverse("aperitivos:video", args=("instalacao-windows",)))


def test_status_code(response_motivacao):
    assert response_motivacao.status_code == 200


def test_titulo_video_motivacao(response_motivacao):
    assert_contains(response_motivacao, "Video Aperitivo: Motivação")


def test_conteudo_video_motivacao(response_motivacao):
    assert_contains(
        response_motivacao,
        '<iframe src="https://player.vimeo.com/video/713071205?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"',
    )


def test_titulo_video_instalacao(response_instalacao):
    assert_contains(response_instalacao, "Video Aperitivo: Instalação no Windows")


def test_conteudo_video_instalacao(response_instalacao):
    assert_contains(
        response_instalacao,
        '<iframe src="https://player.vimeo.com/video/714670248?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"',
    )
