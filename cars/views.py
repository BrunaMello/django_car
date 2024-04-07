from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. Todas as views, tem a logica que precisa aplicar para a visualizacao


def cars_view(request):
    return HttpResponse("Hello, world. You're at the cars view.")
