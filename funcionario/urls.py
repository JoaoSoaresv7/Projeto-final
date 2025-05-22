from django.urls import path
from .views import listar_pedidos, processar_pedido_view

urlpatterns = [
    path('fila/', listar_pedidos, name='listar_pedidos'),
    path('processar/', processar_pedido_view, name='processar_pedido'),
]
