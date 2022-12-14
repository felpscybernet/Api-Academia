from django.db import models

class Aluno(models.Model):

    id_Aluno = models.AutoField (primary_key=True)
    nome_Aluno= models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    setor = models.CharField(max_length=11)
    CPF = models.CharField(max_length=11)

def __str__(self):
    return self.nome_Aluno
