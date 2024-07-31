from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PersonaForm
from .models import Persona



# Create your views here.


def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'form_persona.html', {'form': form})

def lista_personas (request):
    personas = Persona.objects.all()
    return render (request, 'listar.html', {'personas':personas })
