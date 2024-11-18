from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html')

def sobre_nosotros(request):
    return render(request, 'inicio/sobre_nosotros.html')

def recomendaciones(request):
    return render(request, 'inicio/recomendaciones.html')

def catalogo(request):
    return render(request, 'inicio/catalogo.html')

def codigo(request):
    return render(request, 'inicio/codigo.html')