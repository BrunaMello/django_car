from django.http import HttpResponse
from django.shortcuts import render
from cars.models import Car

# Create your views here. Todas as views, tem a logica que precisa aplicar para a visualizacao


def cars_view(request):
    # orm fazendo a requisicao no banco de dados igual o select
    #buscando todos os carros disponiveis
    cars = Car.objects.filter(model__contains='Opala')

    return render(
        request=request,
        template_name='cars.html',
        context={'cars': cars}
    )
