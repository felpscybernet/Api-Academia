from django.db import models


class Fabricante(models.Model):
    id_Fabricante = models.AutoField(primary_key=True)
    nome_Fabricante = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=14)
    pais_de_Origem = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    frete = models.CharField(max_length=100)
    data_de_fabricacao = models.CharField(max_length=100)
    codigo_Postal = models.CharField(max_length=100)
    tempo_de_uso = models.CharField(max_length=100)
    defeitos = models.CharField(max_length=100)


def __str__(self):
    return self.nome_Fabricante