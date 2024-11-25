from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido

def pedidos_pendientes(request):
    pedidos = Pedido.objects.filter(estado='pendiente').order_by('fecha_hora')
    return render(request, 'pedidos/pedidos_pendientes.html', {'pedidos': pedidos})


def historial_pedidos(request):
    pedidos = Pedido.objects.filter(estado='realizado').order_by('fecha_hora')
    return render(request, 'pedidos/historial_pedidos.html', {'pedidos': pedidos})


def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)

    if request.method == 'POST':  # Confirmar pedido
        pedido.estado = 'realizado'
        pedido.save()
        return redirect('pedidos:pedidos_pendientes')  # Redirige a la lista de pendientes

    return render(request, 'pedidos/detalle_pedido.html', {'pedido': pedido})