from django import forms
from django.forms import formset_factory

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

class PedidoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    cpf = forms.CharField(label='CPF', max_length=11)
    endereco = forms.CharField(label='Endereço', max_length=200)
    quantidade = forms.IntegerField(label='Quantidade de Pizzas', min_value=1, max_value=6)
    borda = forms.ChoiceField(label='Borda', choices=[
        ('0', 'Sem borda'),
        ('1', 'Catupiry'),
        ('2', 'Cheddar'),
        ('3', 'Doce de leite')
    ])
    tamanho = forms.ChoiceField(label='Tamanho', choices=[
        ('0', 'Grande'),
        ('1', 'Médio'),
        ('2', 'Pequeno')
    ])

class SaborPizzaForm(forms.Form):
    sabor = forms.ChoiceField(label='Sabor da Pizza', choices=SABORES)

PizzaFormSet = formset_factory(SaborPizzaForm, extra=0)