from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class FormularioInscricao(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class FormularioEmpresa(forms.Form):
    name = forms.CharField(
        label = "nome",
        max_length = 80,
        required = True
    )

    email = forms.EmailField(
        label = "cnpj",
        max_length = 30,
        required = True
    )

    cnpj = forms.IntegerField(
        label = "cnpj",
        required = True
    )

    endereco = forms.CharField(
        label = "endereço",
        max_length = 180,
        required = False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()