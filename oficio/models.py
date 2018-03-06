from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import datetime


class Orgao(models.Model):
    nome = models.CharField(max_length=80)
    logo = models.ImageField()
    cnpj = models.IntegerField()
    cidade = models.CharField(max_length=80)
    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=80)
    endereco = models.TextField()
    telefone = models.IntegerField()
    orgao = models.ForeignKey(Orgao, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=80)
    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    ramal = models.IntegerField()
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    def __str__(self):
        return self.nome

class Oficio(models.Model):
    orgao = models.ForeignKey(Orgao, on_delete=models.PROTECT)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    data = models.DateTimeField(default=timezone.now)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.PROTECT)
    para = models.CharField(max_length=80)
    cargo_para = models.CharField(max_length=80)
    assunto = models.CharField(max_length=80)
    texto = models.TextField()
    numero = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(str(self.numero),self.responsavel)