from django.shortcuts import render
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
            borda = form.cleaned_data['borda']
            tamanho = form.cleaned_data['tamanho']

            preco_sabor = PRECO_SABORES.get(sabor, 0)
            preco_borda = BORDAS.get(borda, 0)
            preco_tamanho = TAMANHOS.get(tamanho, 0)

            api_key = '6b3d0d47b20e418388101e31f6fbf7a6'
            coordenadas_usuario = obter_coordenadas(endereco, api_key)

            if coordenadas_usuario:
                lat, lon = coordenadas_usuario
                distancia = haversine(origem_ufa[0], origem_ufa[1], lat, lon)
                distancia_ajustada = distancia * 1.45
                valor_entrega = max(5.00, 5.00 + distancia_ajustada * 0.5)

                tempo_preparo = 15
                velocidade_media_km_min = 60 / 60
                tempo_entrega = distancia_ajustada / velocidade_media_km_min
                estimativa_total = tempo_preparo + tempo_entrega
            else:
                valor_entrega = 5.00
                distancia_ajustada = 0
                estimativa_total = 15

            total_pizza = preco_sabor + preco_borda + preco_tamanho
            total = round(total_pizza * quantidade + valor_entrega, 2)

            contexto = {
                'nome': nome,
                'cpf': cpf,
                'endereco': endereco,
                'quantidade': quantidade,
                'sabor': sabor,
                'borda': borda,
                'tamanho': tamanho,
                'distancia': round(distancia_ajustada, 2),
                'valor_entrega': valor_entrega,
                'total': total,
                'estimativa_total': estimativa_total,
            }
            return render(request, 'cliente/resumo.html', contexto)

    else:
        form = PedidoForm()

    return render(request, 'cliente/fazer_pedido.html', {'form': form})