from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from django.template import RequestContext, loader


def home(request):
    return render(request, 'demo/home.html', {})

def cgi(request):
    return HttpResponse("<p>Hey!</p>")
