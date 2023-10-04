from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import View
from usipav import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("calc", views.calc, name="calc"),
    path("formulario", views.formulario_inscricao, name="formulario"),
    path("formulario_empresa", views.formulario_empresa, name="empresa"),
    path("empresas", views.Empresa.as_view(), name="empresas")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns