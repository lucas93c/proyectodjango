from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30,null=False)
    edad = models.IntegerField(null=False)
    cuil = models.CharField(
        primary_key=True,
        null=False,
        max_length=11, 
        validators=[
            MinLengthValidator(8), 
            RegexValidator(r'^\d{8,11}$', message="El CUIL debe tener entre 8 y 11 dígitos.")
        ]
    )
    domicilio = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    telefono = models.CharField(
        null=False,
        max_length=12,
        validators=[
            MinLengthValidator(8), 
            RegexValidator(r'^\d{8,12}$', message="El teléfono debe tener entre 8 y 12 dígitos.")
        ]
    )
    
    def __str__(self):
        return self.nombre