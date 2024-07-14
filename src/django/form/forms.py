from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'edad', 'cuil', 'domicilio', 'email', 'telefono']
        widgets = {
            'cuil': forms.TextInput(attrs={'maxlength': 11}),
            'nombre': forms.TextInput(attrs={'maxlength': 30}),
            'telefono': forms.TextInput(attrs={'maxlength': 12}),
            'email': forms.EmailInput(),
            'domicilio': forms.TextInput(attrs={'maxlength': 50}),
            'edad': forms.NumberInput(),
        }

    def clean_cuil(self):
        cuil = self.cleaned_data.get('cuil')
        if not cuil.isdigit():
            raise forms.ValidationError('El CUIL debe contener solo números.')
        if not 8 <= len(cuil) <= 11:
            raise forms.ValidationError('El CUIL debe tener entre 8 y 11 dígitos.')
        return cuil

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise forms.ValidationError('El teléfono debe contener solo números.')
        if not 8 <= len(telefono) <= 12:
            raise forms.ValidationError('El teléfono debe tener entre 8 y 12 dígitos.')
        return telefono
