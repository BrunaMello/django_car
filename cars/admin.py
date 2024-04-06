from django.contrib import admin
from cars.models import Car, Brand


# Register your models here. Tem relacao com o admin do django. Tela de administracao de conteudo. Vizualizacao permitidas somente aos admins do sistema.

#listar na view do admin do sistema

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')


#registrar as tabelas e as configuracoes
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)





