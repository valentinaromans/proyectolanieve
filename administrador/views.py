from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

def lista_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'administrador/lista_productos.html', {'productos': productos})

def detalle_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'administrador/detalle_productos.html', {'producto': producto})

@login_required
def crear_productos(request):
    if request.user.perfil.rol in ['administrador']:
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                producto = form.save(commit=False)
#                producto.autor = request.user
                producto.save()
                return redirect('administrador:detalleproductos', pk=producto.pk)
        else:
            form = ProductoForm()
        return render(request, 'administrador/crear_productos.html', {'form': form})
    else:
        return redirect('administrador:listaproductos')

@login_required
def editar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.user.perfil.rol == 'administrador':
        if request.method == 'POST':
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('administrador:detalleproductos', pk=producto.pk)
        else:
            form = ProductoForm(instance=producto)
        return render(request, 'administrador/editar_productos.html', {'form': form})
    else:
        return redirect('administrador:listaproductos')


@login_required
def eliminar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.user.perfil.rol == 'administrador':
        producto.delete()
    return redirect('administrador:listaproductos')


def lista_usuarios(request):
    return render(request, 'inicio/lista_usuarios.html')