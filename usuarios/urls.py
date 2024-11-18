from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]