# from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id) -> None:
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse("aperitivos:video", args=(self.slug,))


videos = {
    v.slug: v
    for v in [
        Video("motivacao", "Video Aperitivo: Motivação", "713071205"),
        Video("instalacao-windows", "Video Aperitivo: Instalação no Windows", "714670248"),
    ]
}


def indice(request):
    return render(request, "aperitivos/indice.html", context={"videos": videos})


def video(request, slug):
    video = videos[slug]
    return render(request, "aperitivos/video.html", context={"video": video})
