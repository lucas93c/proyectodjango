from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona


# Create your views here.

def hola(request):
    return HttpResponse('Hola')

def persona(request, cuil):
    persona= Persona.objects.get(pk=cuil)
    return HttpResponse(persona.full_name)

