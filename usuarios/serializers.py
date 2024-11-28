from rest_framework import serializers
from .models import Perfil

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Perfil
        fields="__all__"