from django.contrib import admin
from django.urls import path
from . import views
from .views import formulario

app_name = 'form' ## namespace

urlpatterns = [
    path('', views.home, name='home'),    
    path ('formulario/', formulario),
]