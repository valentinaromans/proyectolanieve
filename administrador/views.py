from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'administrador/lista_productos.html', {'productos': productos})

def detalle_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'administrador/detalle_productos.html', {'producto': producto})

@login_required
def crear_productos(request):
    if request.user.perfil.rol in 'administrador':
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Producto creado exitosamente.')
                return redirect('administrador:listaproductos')
        else:
            form = ProductoForm()
        return render(request, 'administrador/crear_productos.html', {'form': form})
    else:
        return redirect('administrador:listaproductos')

@login_required
def editar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('administrador:listaproductos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'administrador/editar_productos.html', {'form': form})


@login_required
def eliminar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('administrador:listaproductos')
    return render(request, 'administrador/eliminar_productos.html', {'producto': producto})