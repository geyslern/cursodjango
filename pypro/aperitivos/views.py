# from django.http import HttpResponse
from pypro.aperitivos.models import Video
from django.shortcuts import render, get_object_or_404


def indice(request):
    videos = Video.objects.order_by("creation").all()
    resp = render(request, "aperitivos/indice.html", context={"videos": videos})
    return resp


def video(request, video_slug):
    video = get_object_or_404(Video, slug=video_slug)
    return render(request, "aperitivos/video.html", context={"video": video})
