from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)  # armazenaremos com hash

    def __str__(self):
        return self.nome