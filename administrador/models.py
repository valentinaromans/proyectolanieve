from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
#    imagen_url = models.URLField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.nombre
    