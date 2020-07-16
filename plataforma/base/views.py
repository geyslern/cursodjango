# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Hello Django. It works!</body></html>', content_type='text/html; charset=UTF-8')
