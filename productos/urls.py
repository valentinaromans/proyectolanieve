from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('nuevo/', views.crear_producto, name='crear_producto'),
    path('<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]