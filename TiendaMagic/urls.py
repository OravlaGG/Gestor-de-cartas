"""
URL configuration for TiendaMagic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GestorCartas.views import home, login_user, logout_user, coleccion_usuario, agregar_a_coleccion, eliminar_coleccion, editar_coleccion

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', home),
   path('home/', home),
   path('login',login_user, name="login"),
   path('logout',logout_user, name="logout"),
   path("mi-coleccion/", coleccion_usuario, name="coleccion_usuario"),
   path("agregar/<int:carta_id>/", agregar_a_coleccion, name="agregar_a_coleccion"),
   path("eliminar/<int:pk>/", eliminar_coleccion, name="eliminar_coleccion"),
   path("editar/<int:pk>/", editar_coleccion, name="editar_coleccion"),
]

#Add Django site authentication urls (for login, logout, password management)

