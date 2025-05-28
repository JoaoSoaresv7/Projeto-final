from django.urls import path
from .views import registrar_funcionario,   listar_pedidos, processar_pedido_view, logar_func


urlpatterns = [
    path('registro/', registrar_funcionario, name='registro_funcionario'),
    path('fila/', listar_pedidos, name='listar_pedidos'),
    path('processar/', processar_pedido_view, name='processar_pedido'),
    path('login/', logar_func, name='login_funcionario'),
]
