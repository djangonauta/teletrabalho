from django.conf import settings
from django.db import models


class Unidade(models.Model):

    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Complexidade(models.Model):

    class Tipos(models.IntegerChoices):
        ALTA = 1
        MEDIA = 2
        BAIXA = 3

    tipo = models.IntegerField(choices=Tipos.choices, null=False)
    criterios = models.TextField()

    def __str__(self):
        return self.Tipos(self.tipo).name


class Atividade(models.Model):

    unidade = models.ForeignKey(Unidade, related_name='atividades', on_delete=models.CASCADE)
    complexidade = models.ForeignKey(Complexidade, related_name='atividades', on_delete=models.CASCADE)

    nome = models.CharField(max_length=255)
    tempo_presencial = models.IntegerField()
    tempo_teletrabalho = models.IntegerField()

    def __str__(self):
        return f'{self.unidade.nome} - {self.nome}'


class PlanoTrabalho(models.Model):

    servidor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='planos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    atividades = models.ManyToManyField(Atividade, related_name='planos_trabalho')

    def __str__(self):
        return self.nome
