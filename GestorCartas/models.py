from django.db import models
from django.contrib.auth.models import User

#No puede existir la misma edición 2 veces
class Edicion(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    codigo = models.CharField(max_length=10, unique=True)
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

#No puede repetirse los colores
class Color(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

#No puede existir la misma carta 2 veces 
class Carta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    coste_mana = models.CharField(max_length=20, blank=True)
    tipo = models.CharField(max_length=50)
    rareza = models.CharField(max_length=20)
    edicion = models.ManyToManyField(Edicion)
    colores = models.ManyToManyField(Color, blank=True)

    def __str__(self):
        return self.nombre


class Coleccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carta = models.ForeignKey(Carta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    estado = models.CharField(
        max_length=20,
        choices=[
            ("NM", "Near Mint"),
            ("LP", "Lightly Played"),
            ("MP", "Moderately Played"),
            ("HP", "Heavily Played"),
            ("DMG", "Damaged"),
        ],
        default="NM"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "carta"],
                name="unique_usuario_carta"
            )
        ]


    def __str__(self):
        return f"{self.usuario.username} - {self.carta.nombre} x{self.cantidad}"
