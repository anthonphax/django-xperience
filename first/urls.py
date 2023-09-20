from django.contrib import admin
from django.urls import include, path
from usipav import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("calc", views.calc, name="calc"),
    path("formulario", views.formulario_inscricao, name="formulario"),
    path("formulario_empresa", views.formulario_empresa, name="empresa"),
    path("empresas", views.empresas, name="empresas")
]
