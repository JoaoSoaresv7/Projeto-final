from django.urls import path
from .views import listar_pedidos, processar_pedido_view, logar_func, registrar_funcionario

urlpatterns = [
    path('fila/', listar_pedidos, name='listar_pedidos'),
    path('processar/', processar_pedido_view, name='processar_pedido'),
    path('login/', logar_func, name='logar_func'),
    path('registro/', registrar_funcionario, name='registro_funcionario')
]
