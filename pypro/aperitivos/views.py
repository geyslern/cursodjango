from django.http import HttpResponse
from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '713071205?h=dbdac475f3'}
    return render(request, 'aperitivos/video.html', context={'video': video})