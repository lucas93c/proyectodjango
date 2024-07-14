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
def formulario_view(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form:success')
    else:
        form = PersonaForm()
    return render(request, 'form/formulario.html', {'form': form})

def success_view(request):
    return render(request, 'form/success.html')
"""Fin formulario"""

def home(request):
    return render(request, 'form/base.html')