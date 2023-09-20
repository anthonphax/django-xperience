from django.contrib import admin
from .models import Topico, Pagina, RegistroAcesso, Empresa, Funcionario


class FuncAdmin(admin.ModelAdmin):
    fields: [ 'name', 'email', 'cpf']
    list_display: ['email', 'cpf']


admin.site.register(Topico)
admin.site.register(Pagina)
admin.site.register(RegistroAcesso)
admin.site.register(Empresa)
admin.site.register(Funcionario, FuncAdmin)


