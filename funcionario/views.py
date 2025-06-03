from django.shortcuts import render, redirect
from cliente.models import Pedido
from django.contrib import messages
from django.http import HttpResponse

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

import logging

logger = logging.getLogger('myapp')  # use o nome definido no settings.py

def minha_view(request):
    logger.debug("Isso é uma mensagem de DEBUG")
    logger.info("Isso é uma mensagem de INFO")
    logger.warning("Isso é uma mensagem de WARNING")
    logger.error("Isso é uma mensagem de ERROR")
    logger.critical("Isso é uma mensagem de CRITICAL")
    return HttpResponse("Veja os logs para mais informações.")

