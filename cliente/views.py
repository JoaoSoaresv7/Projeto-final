from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm
from .utils import obter_coordenadas, haversine

origem_ufa = (-15.7913, -47.9300)

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

            # Converter os valores legíveis para os códigos usados no model
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
            return redirect('fila_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'cliente/fazer_pedido.html', {'form': form})

API_KEY = '6b3d0d47b20e418388101e31f6fbf7a6'

def fila_pedidos(request):
    pedidos = Pedido.objects.filter(concluido=False).order_by('id')

    velocidade_media_kmh = 60
    preco_frete_por_km = 0.45
    

    for pedido in pedidos:
        coord_cliente = obter_coordenadas(pedido.endereco, API_KEY)
        
        if coord_cliente:
            lat1, lon1 = origem_ufa
            lat2, lon2 = coord_cliente
            distancia_km = haversine(lat1, lon1, lat2, lon2)
            distancia_km *= 1.45
            pedido.quilometragem = round(distancia_km, 1)
            pedido.tempo_entrega = int((distancia_km / velocidade_media_kmh) * 60) + 30
            pedido.preco_frete = round(distancia_km * preco_frete_por_km, 2)
        else:
            pedido.quilometragem = None
            pedido.tempo_entrega = None
            pedido.preco_frete = None

        preco_sabor = PRECO_SABORES.get(pedido.sabor1, 0)
        preco_borda = BORDAS.get(pedido.get_borda_display(), 0)
        preco_tamanho = TAMANHOS.get(pedido.get_tamanho_display(), 0)

        pedido.preco_geral = round(
            pedido.quantidade * (preco_sabor + preco_borda + preco_tamanho) +
            (pedido.preco_frete if pedido.preco_frete else 0), 2
        )

    return render(request, 'cliente/fila_pedidos.html', {'pedidos': pedidos})

def cardapio(request):
    return render(request, 'cliente/cardapio.html')