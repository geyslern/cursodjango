from django.http import HttpResponse
from django.shortcuts import render


def video(request, slug):
    return render(request, 'aperitivos/video.html')