from django.urls import path
from . import views

app_name = 'administrador'
urlpatterns = [
    path('listaproductos/', views.lista_productos, name='listaproductos'),
    path('crearproductos/', views.crear_productos, name='crearproductos'),
    path('detalleproductos/', views.detalle_productos, name='detalleproductos'),
    path('editarproductos/', views.editar_productos, name='editarproductos'),
    path('eliminarproductos/', views.eliminar_productos, name='eliminarproductos'),
    path('listausuarios/', views.lista_usuarios, name='listausuarios'),
]