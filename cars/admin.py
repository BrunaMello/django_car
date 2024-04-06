from django.contrib import admin
from cars.models import Car


# Register your models here. Tem relacao com o admin do django. Tela de administracao de conteudo. Vizualizacao permitidas somente aos admins do sistema.

#listar na view do admin do sistema
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

#registrar as tabelas e as configuracoes
admin.site.register(Car, CarAdmin)

