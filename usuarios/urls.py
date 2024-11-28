from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


    path('api_articulos/', views.api_articulos, name='api_articulos'),
    path('api_articulos_detalle/<int:pk>/', views.api_articulos_detalle, name='api_articulos_detalle'),
]