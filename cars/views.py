from django.http import HttpResponse
from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm


# Create your views here. Todas as views, tem a logica que precisa aplicar para a visualizacao


def cars_view(request):
    # orm fazendo a requisicao no banco de dados igual o select
    # buscando todos os carros disponiveis
    cars = Car.objects.all().order_by('model')

    # verificar se tem busca especifica
    search = request.GET.get('search')

    # se sim entra no if
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')

    return render(
        request=request,
        template_name='cars.html',
        context={'cars': cars}
    )


def new_car_view(request):
    new_car_form = CarForm()

    return render(
        request=request,
        template_name='new_car.html',
        context={'new_car_form': new_car_form}
    )
