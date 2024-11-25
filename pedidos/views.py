from django.shortcuts import render

def pedidos_pendientes(request):
    return render(request, 'pedidos/pedidos_pendientes.html')

def historial_pedidos(request):
    return render(request, 'pedidos/historial_pedidos.html')