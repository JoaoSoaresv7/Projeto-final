from django.shortcuts import render, redirect
from cliente.models import Pedido
from django.contrib import messages

def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('id')  # Ordem crescente, do mais antigo para o mais novo
    return render(request, 'funcionario/listar_pedidos.html', {'pedidos': pedidos})

def processar_pedido_view(request):
    if request.method == "POST":
        pedido = Pedido.objects.first()
        if pedido:
            pedido.delete()
            messages.success(request, "Pedido processado com sucesso.")
        else:
            messages.warning(request, "Nenhum pedido para processar.")
    return redirect('listar_pedidos')
