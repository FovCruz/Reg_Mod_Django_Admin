from django import forms
#se importa la clase persona desde models.py (alojado en app web)
from .models import Persona


# se crea la clase PersonaForm con 2 atributos
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre','edad','email']
