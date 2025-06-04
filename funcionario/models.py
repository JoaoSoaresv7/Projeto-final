from django.db import models
from cliente.models import Pedido 

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Etiqueta(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    acao = models.CharField(max_length=100) 
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.acao} - {self.pedido.nome if self.pedido else 'Pedido removido'}"
