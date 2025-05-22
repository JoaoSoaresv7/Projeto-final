from django.urls import path
from . import views

urlpatterns = [
    path('fazer/', views.fazer_pedido_view, name='fazer_pedido'),
    path('confirmado/', views.pedido_confirmado_view, name='pedido_confirmado'),

]
