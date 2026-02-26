from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from GestorCartas.models import Carta
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home (request): # Pinta una página con render, también hay que darlo de
    cartas = Carta.objects.all()
    return render(request, "index.html", {"cartas": cartas})
  
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
                    return redirect("home/")
                else:
                    messages.error(request, 'Usuario Inactivo')
            else:
                messages.error(request, 'Usuario no existe con esos credenciales')
        else:
            messages.error(request, 'Usuario o Contraseña es Incorrecto')

    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Has hecho Logout')
    
    return redirect("home/")