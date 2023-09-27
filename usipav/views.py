from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
import django.views.generic.edit as django_edit
from .forms import *
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

def formulario_empresa(request):
    return render(request, 'formEmpresa.html', context={'form': FormularioEmpresa})

def index(request):
    return render(request, 'calc.html', context={'index': index})

def calc(request):
    c = {'insert' : 'calculadora'}
    return render (request, 'calc.html', context=c)

def empresas(request):
    _list = Empresa.objects.all()
    c = {'empresas': _list}
    return render(request, 'index.html', context=c)

def harry(request):
    c = {'insert' : 'harry potter'}
    return render (request, 'hp1.html', context=c)

class Empresa(ListView):
    model = Empresa
    template_name = 'CRUD/empresa_list.html'








    # def criar_empresa(request):
    #     if request.method == 'POST':
    #         form = FormularioEmpresa(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('lista_empresas')
    #     else:
    #         form = FormularioEmpresa()
    #     return render(request, 'success.html', {'form': form})

    # def atualizar_empresa(request, empresa_id):
    #     empresa = get_object_or_404(Empresa, pk=empresa_id)
    #     if request.method == 'POST':
    #         form = FormularioEmpresa(request.POST, instance=empresa)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('detalhes_empresa', empresa_id=empresa_id)
    #     else:
    #         form = FormularioEmpresa(instance=empresa)
    #     return render(request, 'atualizar_empresa.html', {'form': form, 'empresa': empresa})
