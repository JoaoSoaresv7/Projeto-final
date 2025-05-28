from django.db import models

class Pedido(models.Model):
    TAMANHOS = [('0', 'Grande'), ('1', 'Médio'), ('2', 'Pequeno')]
    BORDAS = [('0', 'Sem borda'), ('1', 'Catupiry'), ('2', 'Cheddar'), ('3', 'Doce de leite')]
    SABORES = [
        ('01', 'Portuguesa'),
        ('02', 'Chocolate'),
        ('03', 'Peixe'),
        ('04', 'Margarita'),
        ('05', 'Quatro-queijos'),
        ('06', 'Marguerita'),
        ('07', 'Calabresa'),
        ('08', 'Peperoni'),
        ('09', 'Alho e óleo'),
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    borda = models.CharField(max_length=1, choices=BORDAS)
    tamanho = models.CharField(max_length=1, choices=TAMANHOS)
    sabor1 = models.CharField(max_length=2, choices=SABORES, default='01')
    concluido = models.BooleanField(default=False)  # ✅ Adicionado para o sistema de conclusão
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido de {self.nome} - {self.quantidade} pizza(s)'

class Pizza(models.Model):
    SABORES = Pedido.SABORES

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pizzas')
    sabor = models.CharField(max_length=2, choices=SABORES)

    def __str__(self):
        return f'{self.get_sabor_display()} do pedido {self.pedido.id}'
