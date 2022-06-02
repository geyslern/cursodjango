# from django.http import HttpResponse
from pypro.aperitivos.models import Video
from django.shortcuts import render


videos = {
    v.slug: v
    for v in [
        Video(slug="motivacao", titulo="Video Aperitivo: Motivação", vimeo_id="713071205"),
        Video(slug="instalacao-windows", titulo="Video Aperitivo: Instalação no Windows", vimeo_id="714670248"),
    ]
}


def indice(request):
    return render(request, "aperitivos/indice.html", context={"videos": videos})


def video(request, slug):
    video = videos[slug]
    return render(request, "aperitivos/video.html", context={"video": video})
