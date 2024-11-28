# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .models import Perfil
from .forms import RegistroForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password']) 
            user.save()
            # Crear el perfil asociado al usuario
            perfil = Perfil.objects.create(user=user, rol=form.cleaned_data['rol'], nombre=form.cleaned_data['nombre'], apellido=form.cleaned_data['apellido'])
            perfil.save()
            
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            #return redirect('usuarios:login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('productos:lista_productos')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('usuarios:login')




from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ArticuloSerializer

@api_view(["GET","POST"])
def api_articulos(request):
    if request.method=="GET":
        articulos=Perfil.objects.all()
        serializer=ArticuloSerializer(articulos,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
def api_articulos_detalle(request,pk):
    try:
        articulo=Perfil.objects.get(pk=pk)
    except Exception as e:
        print(f"Error {e}")
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=ArticuloSerializer(articulo)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=ArticuloSerializer(articulo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        articulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)