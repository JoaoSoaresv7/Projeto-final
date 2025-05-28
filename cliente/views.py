from django.shortcuts import render, redirect, get_object_or_404
from .forms import PedidoForm
from .utils import obter_coordenadas, haversine
from .models import Pedido

# Coordenadas fixas da origem (por exemplo: UDF)
origem_ufa = (-15.7913, -47.9300)

# Preços definidos no front, podem ser usados para cálculo se necessário
BORDAS = {
    'Sem borda': 0.00,
    'Catupiry': 5.99,
    'Cheddar': 5.99,
    'Doce de leite': 8.99
}
TAMANHOS = {
    'Grande': 10.00,
    'Médio': 7.00,
    'Pequeno': 5.00
}
PRECO_SABORES = {
    '01': 29.99, '02': 50.00, '03': 29.99,
    '04': 39.99, '05': 39.99, '06': 29.99,
    '07': 29.99, '08': 50.00, '09': 29.99
}


def fazer_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['cliente_nome']
            cpf = form.cleaned_data['cliente_cpf']
            endereco = form.cleaned_data['endereco']
            quantidade = int(form.cleaned_data['quantidade_pizzas'])
            sabor = form.cleaned_data['sabor']
            borda_legivel = form.cleaned_data['borda']
            tamanho_legivel = form.cleaned_data['tamanho']

            # Mapeia o valor visível para o código usado no banco
            borda_codigo = next(k for k, v in Pedido.BORDAS if v == borda_legivel)
            tamanho_codigo = next(k for k, v in Pedido.TAMANHOS if v == tamanho_legivel)

            Pedido.objects.create(
                nome=nome,
                cpf=cpf,
                endereco=endereco,
                quantidade=quantidade,
                sabor1=sabor,
                borda=borda_codigo,
                tamanho=tamanho_codigo,
                concluido=False
            )

            return redirect('fila_pedidos')  # Redireciona para a fila do cliente
    else:
        form = PedidoForm()

    return render(request, 'cliente/fazer_pedido.html', {'form': form})


def fila_pedidos(request):
    # Exibe apenas os pedidos que ainda não foram concluídos
    pedidos = Pedido.objects.filter(concluido=False).order_by('id')
    return render(request, 'cliente/fila_pedidos.html', {'pedidos': pedidos})
