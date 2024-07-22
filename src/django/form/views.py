from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Persona
from .forms import PersonaForm

# Create your views here.

def hola(request):
    return HttpResponse('Hola')

def persona(request, cuil):
    persona= Persona.objects.get(pk=cuil)
    return HttpResponse(persona.full_name)

"""Formulario"""
def formulario(request):
    cargado=False
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            cargado=True
            form = PersonaForm()
    else:
        form = PersonaForm()
    return render(request, 'formulario.html', {'form': form, 'cargado':cargado})

"""Fin formulario"""

def home(request):
    return render(request, 'base.html')

