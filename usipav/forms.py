from django import forms
from .models import *

class FormularioInscricao(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'