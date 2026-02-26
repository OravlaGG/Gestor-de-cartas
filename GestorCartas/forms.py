from django import forms
from .models import Coleccion

class ColeccionEditForm(forms.ModelForm):
    class Meta:
        model = Coleccion
        fields = ["cantidad", "estado"]
