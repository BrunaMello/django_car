from django.shortcuts import render, redirect
from django.views import View

from cars.forms import CarModelForm
from cars.models import Car


# Create your views here. Todas as views, tem a logica que precisa aplicar para a visualizacao

class CarsView(View):

    def get(self, request):
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
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')

    else:
        new_car_form = CarModelForm()
    return render(
        request=request,
        template_name='new_car.html',
        context={'new_car_form': new_car_form}
    )
