from django import forms

SABORES = [
    ('01', 'Portuguesa'), ('02', 'Chocolate'), ('03', 'Peixe'),
    ('04', 'Margarita'), ('05', 'Quatro-queijos'), ('06', 'Marguerita'),
    ('07', 'Calabresa'), ('08', 'Peperoni'), ('09', 'Alho e óleo')
]

BORDAS = [
    ('Sem borda', 0.00),
    ('Catupiry', 5.99),
    ('Cheddar', 5.99),
    ('Doce de leite', 8.99)
]

TAMANHOS = [
    ('Grande', 10.00),
    ('Médio', 7.00),
    ('Pequeno', 5.00)
]

QUANTIDADES = [(i, str(i)) for i in range(1,7)]

class PedidoForm(forms.Form):
    cliente_nome = forms.CharField(label="Nome do Cliente", max_length=100)
    cliente_cpf = forms.CharField(label="CPF", max_length=14)
    endereco = forms.CharField(label="Endereço", max_length=255)
    quantidade_pizzas = forms.ChoiceField(label="Quantidade de pizzas", choices=QUANTIDADES)
    sabor = forms.ChoiceField(label="Sabor da pizza", choices=SABORES)
    borda = forms.ChoiceField(label="Borda", choices=[(b[0], b[0]) for b in BORDAS])
    tamanho = forms.ChoiceField(label="Tamanho da pizza", choices=[(t[0], t[0]) for t in TAMANHOS])
