from django.urls import path
from . import views
from .views import cardapio

urlpatterns = [
    path('fa_pedido', views.fazer_pedido, name='fa_pedido'),
    path('fila/', views.fila_pedidos, name='fila_pedidos'),
    path('cardapio/', cardapio, name='cardapio'),
]
