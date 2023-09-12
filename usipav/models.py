from django.db import models

class Topico(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Pagina(models.Model):
    tp = models.ForeignKey(Topico, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Empresa(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    cnpj = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Funcionario(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class RegistroAcesso(models.Model):
    pg = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)