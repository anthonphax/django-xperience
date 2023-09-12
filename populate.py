from datetime import datetime
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first.settings')
django.setup()
import re
# from random import randint, choices
# from string import ascii_uppercase, digits
import unidecode
from usipav.models import Topico, Pagina, RegistroAcesso, Empresa, Funcionario
from faker import Faker as mock
from validate_docbr import CPF, CNPJ

_range = 10

class Generator:
    f = mock('pt_BR')
    cpf = CPF()
    cnpj = CNPJ()

    def gerar_razao_social(self, r):
        list_names = []
        while len(list_names) < r:
            valor = self.f.company()
            list_names.append(valor)
        return list_names

    def gerar_nome(self, r):
        list_nomes = []
        while len(list_nomes) < r:
            valor = self.f.name()
            list_nomes.append(valor)
        return list_nomes

    def gerar_enderecos(self, r):
        list_enderecos = []
        while len(list_enderecos) < r:
            valor = self.f.address()
            list_enderecos.append(valor)
        return list_enderecos
            
    def gerar_cpf(self, r):
        lista = []
        while len(lista) < r:
            valor = self.f.cpf()
            valor = re.sub('[.,-]', '', valor)
            if self.cpf.validate(str(valor)):
                lista.append(str(valor))
        return lista

    def gerar_cnpj(self, r):
        list_cnpj = []
        while len(list_cnpj) < r:
            valor = self.f.cnpj()
            valor = re.sub('[.,-,/]', '', valor)
            if self.cnpj.validate(str(valor)):
                list_cnpj.append(valor)
        return list_cnpj
    
    def gerar_email(self, r):
        list_email = []
        while len(list_email) < r:
            y = self.f.email()
            x = unidecode.unidecode(y)
            list_email.append(x)
        return list_email #list of string

    # def gerar_senha(self, n):
    #     x = ''.join(choices(ascii_uppercase + digits, k=n))
    #     with open('../password.txt', 'w') as file:
    #         file.write(str(x))

g = Generator()
razoes = g.gerar_razao_social(_range)
cnpjs = g.gerar_cnpj(_range)
cpfs = g.gerar_cpf(_range)
emails = g.gerar_email(_range)
enderecos = g.gerar_enderecos(_range)
nomes = g.gerar_nome(_range)

print(razoes[1])
print(cnpjs[1])
print(cpfs[1])
print(emails[1])
print(enderecos[1])
print(nomes[1])


for i in range(_range):
    t = Topico.objects.get_or_create(name=nomes[i])[0]
    p = Pagina.objects.get_or_create(tp=t,name=nomes[i])[0]
    f = Funcionario.objects.get_or_create(name=razoes[i], email=emails[i], cpf=cpfs[i], endereco=enderecos[i])[0] 
    e = Empresa.objects.get_or_create(name=razoes[i], email=emails[i], cnpj=cnpjs[i], endereco=enderecos[i])[0]
    _ = RegistroAcesso.objects.get_or_create(pg=p, date=datetime.now())[0]
    
    t.save()
    p.save()
    f.save()
    e.save()
    _.save()
