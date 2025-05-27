from django.urls import path
from . import views

urlpatterns = [
    path('fa_pedido', views.fazer_pedido, name='fa_pedido'),
]