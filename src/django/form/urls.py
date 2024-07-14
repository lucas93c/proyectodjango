from django.contrib import admin
from django.urls import path
from . import views

app_name = 'form' ## namespace

urlpatterns = [
    path('hola/', views.hola),
    path('persona/<int:cuil>', views.persona),
    path('', views.formulario_view, name='formulario'),
    path('success/', views.success_view, name='success'),
    path('', views.home, name='home')
]