from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. Todas as views, tem a logica que precisa aplicar para a visualizacao


def cars_view(request):
    return render(
        request=request,
        template_name='cars.html',
        context={'cars': {'model': 'Astra 2.0'}}
    )
