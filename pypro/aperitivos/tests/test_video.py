import pytest
from django.urls import reverse
from django.test import Client
from pypro.django_assertions import assert_contains

@pytest.fixture
def response(client:Client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(response):
    assert response.status_code == 200

def test_titulo_video(response):
    assert_contains(response, 'Video Aperitivo: Motivação')

def test_conteudo_video(response):
    assert_contains(response, '<iframe src="https://player.vimeo.com/video/713071205?h=dbdac475f3"')
