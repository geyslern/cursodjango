from django.http import HttpResponse
from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '713071205'},
        'instalacao-windows': {'titulo': 'Video Aperitivo: Instalação no Windows', 'vimeo_id': '714670248'}
    }

    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
