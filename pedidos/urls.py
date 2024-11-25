from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('pendientes/', views.pedidos_pendientes, name='pedidospendientes'),
    path('historial/', views.historial_pedidos, name='historialpedidos'),
    path('<int:pk>/', views.detalle_pedido, name='detallepedido'),
    path('<int:pedido_id>/confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
]