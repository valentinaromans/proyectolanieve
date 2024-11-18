from django.urls import path
from . import views

app_name = 'vendedor'
urlpatterns = [
    path('verproductos/', views.ver_productos, name='verproductos'),
    path('pedidospendientes/', views.pedidos_pendientes, name='pedidospendientes'),
    path('historialpedidos/', views.historial_pedidos, name='historialpedidos'),
    path('ayudasoporte/', views.ayuda_soporte, name='ayudasoporte'),
]