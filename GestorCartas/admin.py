from django.contrib import admin

# Register your models here.
from GestorCartas.models import Edicion
from GestorCartas.models import Carta
from GestorCartas.models import Color


admin.site.register(Edicion)
admin.site.register(Color)
admin.site.register(Carta)