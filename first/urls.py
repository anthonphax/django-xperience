from django.contrib import admin
from django.urls import include, path
from usipav import views

app_name = "basic_app"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("calc", views.calc, name="calc"),
    path("harry", views.harry, name="harry"),
    path("formulario", views.formulario_inscricao, name="formulario"),
    path("empresas", views.index, name="empresas")
]
