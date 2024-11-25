from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('pendientes/', views.pedidos_pendientes, name='pedidospendientes'),
    path('historial/', views.historial_pedidos, name='historialpedidos'),
]