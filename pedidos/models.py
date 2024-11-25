from django.db import models

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)  # o un ForeignKey si tienes usuarios
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('realizado', 'Realizado')])
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.producto} ({self.estado})"
