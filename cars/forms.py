from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    # funcoes de validacao de campo sempre comecam com clean_ o nome do campo
    def clean_value(self):
        # self e uma instancia do form
        # cleaned data ja sao os dados limpos
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error(
                field='value',
                error='Value must be greater than or equal to 20000'
            )
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error(
                field='factory_year',
                error='Model year must be greater than or equal to 1975'
            )
        return factory_year


