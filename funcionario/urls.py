<<<<<<< HEAD
from django.urls import path
from .views import (
    listar_pedidos, processar_pedido_view,
    logar_func, registrar_funcionario, home_page, logout_funcionario, concluir_pedido, excluir_pedido
)

urlpatterns = [
    path('fila/', listar_pedidos, name='listar_pedidos'),
    path('processar/', processar_pedido_view, name='processar_pedido'),
    path('login/', logar_func, name='login_funcionario'),  # nome corrigido
    path('logout/', logout_funcionario, name='logout_funcionario'),  # logout opcional
    path('registro/', registrar_funcionario, name='registro_funcionario'),
    path('', home_page, name='home_page'),
    path('concluir/<int:pedido_id>/', concluir_pedido, name='concluir_pedido'),
    path('excluir/<int:pedido_id>/', excluir_pedido, name='excluir_pedido'),

]
=======
from django.urls import path
from .views import (
    listar_pedidos, processar_pedido_view,
    logar_func, registrar_funcionario, home_page, logout_funcionario, concluir_pedido, excluir_pedido
)

urlpatterns = [
    path('fila/', listar_pedidos, name='listar_pedidos'),
    path('processar/', processar_pedido_view, name='processar_pedido'),
    path('login/', logar_func, name='login_funcionario'),  # nome corrigido
    path('logout/', logout_funcionario, name='logout_funcionario'),  # logout opcional
    path('registro/', registrar_funcionario, name='registro_funcionario'),
    path('', home_page, name='home_page'),
    path('concluir/<int:pedido_id>/', concluir_pedido, name='concluir_pedido'),
    path('excluir/<int:pedido_id>/', excluir_pedido, name='excluir_pedido'),

]
>>>>>>> 81e4968abde002e858a3addca30aac4f09a89e45
