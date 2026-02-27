from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from GestorCartas.models import Carta, Coleccion
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ColeccionEditForm

# Create your views here.

def home (request): # Pinta una página con render, también hay que darlo de
    cartas = Carta.objects.all()
    return render(request, "index.html", {"cartas": cartas})

# Usu de prueba:
#   Nombre: prueba
#   Password: Prueba.Prueba
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            user = None
            messages.error(request, 'Usuario no existe')

        if user:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    cartas = Carta.objects.all()
                    return redirect("home")
                else:
                    messages.error(request, 'Usuario Inactivo')
            else:
                messages.error(request, 'Usuario no existe con esos credenciales')
        else:
            messages.error(request, 'Usuario o Contraseña es Incorrecto')

    return render(request,'login.html')

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Has hecho Logout')
    
    return redirect("home")

@login_required
def coleccion_usuario(request):
    coleccion = Coleccion.objects.filter(usuario=request.user).select_related("carta")
    return render(request, "coleccion.html", {"coleccion": coleccion})


@login_required
def agregar_a_coleccion(request, carta_id):
    carta = get_object_or_404(Carta, id=carta_id)

    # Buscar si ya existe en la colección del usuario
    coleccion_item, creado = Coleccion.objects.get_or_create(
        usuario=request.user,
        carta=carta,
        defaults={"cantidad": 1}
    )

    # Si ya existía, aumentar cantidad
    if not creado:
        coleccion_item.cantidad += 1
        coleccion_item.save()

    return redirect("home")


@login_required
def eliminar_coleccion(request, pk):
    item = get_object_or_404(Coleccion, pk=pk, usuario=request.user)
    item.delete()
    return redirect("coleccion_usuario")

@login_required
def editar_coleccion(request, pk):
    item = get_object_or_404(Coleccion, pk=pk, usuario=request.user)

    if request.method == "POST":
        form = ColeccionEditForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("coleccion_usuario")
    else:
        form = ColeccionEditForm(instance=item)

    return render(request, "editar_coleccion.html", {
        "form": form,
        "item": item
    })