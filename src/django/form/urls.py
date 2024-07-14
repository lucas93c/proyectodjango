from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.hola),
    path('persona/<int:cuil>', views.persona)
]