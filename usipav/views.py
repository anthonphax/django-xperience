from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormularioInscricao
from .models import *


def formulario_inscricao(request):
    form = FormularioInscricao()
    if request.method == 'POST':
        form = FormularioInscricao(request.POST)
        if form.is_valid():
            print("Sucesso")
            form.save(commit=True)
            return index(request)
        else:
            print("algo errado")

    return render(request, 'form.html', context={'form': form})

def index(request):
    return render("Hello, world!!!")

def empresas(request):
    _list = Empresa.objects.all()
    c = {'empresas': _list}
    return render(request, 'index.html', context=c)

def calc(request):
    c = {'insert' : 'calculadora'}
    return render (request, 'calc.html', context=c)

def harry(request):
    c = {'insert' : 'harry potter'}
    return render (request, 'hp1.html', context=c)

