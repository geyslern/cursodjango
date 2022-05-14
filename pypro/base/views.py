from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    return HttpResponse("<html><body>It works!</body></html>")
