from django.shortcuts import render

# Create your views here.
def pedidos_pendientes(request):
    return render(request, 'vendedor/pedidos_pendientes.html')

def ver_productos(request):
    return render(request, 'vendedor/ver_productos.html')

def historial_pedidos(request):
    return render(request, 'vendedor/historial_pedidos.html')

def ayuda_soporte(request):
    return render(request, 'vendedor/ayuda_soporte.html')