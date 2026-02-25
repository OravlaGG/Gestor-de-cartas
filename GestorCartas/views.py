from django.shortcuts import render
from django.contrib.auth.models import User
from GestorCartas.models import Carta

# Create your views here.

def home (request): # Pinta una página con render, también hay que darlo de
    cartas = Carta.objects.all()
    return render(request, "index.html", {"cartas": cartas})
    return render(request,'index.html')
  
def login(request):
    return render(request,'login/index.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except user.DoesNotExist:
            user = None
            message.error(request, 'Usuario no existe')

        if user:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
                else:
                    message.error(request, 'Usuario Inactivo')
            else:
                message.error(request, 'Usuario no existe con esos credenciales')
        else:
            message.error(request, 'Usuario o Contraseña es Incorrecto')

    return render(request, 'login/index.html')