from django.contrib import admin
from .models import Topico, Pagina, RegistroAcesso, Empresa, Funcionario

admin.site.register(Topico)
admin.site.register(Pagina)
admin.site.register(RegistroAcesso)
admin.site.register(Empresa)
admin.site.register(Funcionario)
