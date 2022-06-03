import pytest
from model_mommy import mommy
from django.urls import reverse
from pypro.django_assertions import assert_contains
from pypro.aperitivos.models import Video


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def response_video(client, video):
    return client.get(reverse("aperitivos:video", args=(video.slug,)))


@pytest.fixture
def response_video_nao_existe(client, video):
    return client.get(reverse("aperitivos:video", args=(f"{video.slug}_nao_existe",)))


def test_status_code(response_video):
    assert response_video.status_code == 200


def test_status_code_404(response_video_nao_existe):
    assert response_video_nao_existe.status_code == 404


def test_titulo_video_motivacao(response_video, video):
    assert_contains(response_video, video.titulo)


def test_conteudo_video_motivacao(response_video, video):
    assert_contains(
        response_video,
        f'"https://player.vimeo.com/video/{ video.vimeo_id }?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"',
    )
