

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('funcionario/', include('funcionario.urls')), 
    path('', include('home_pizzaria.urls')),
]
