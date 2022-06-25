import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains
from pypro.aperitivos.models import Video
from model_bakery import baker


@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture
def response_indice(client, videos):
    return client.get(reverse("aperitivos:indice"))


def test_status_code(response_indice):
    assert response_indice.status_code == 200


def test_titulo_indice(response_indice):
    assert_contains(response_indice, "Vídeos Aperitivos")


def test_titulos_videos(response_indice, videos):
    for video in videos:
        assert_contains(response_indice, video.titulo)


def test_link_motivacao(response_indice, videos):
    for video in videos:
        video_link = reverse("aperitivos:video", args=(video.slug,))
        assert_contains(response_indice, f'href="{video_link}"')
