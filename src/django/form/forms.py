from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'finput'}),
        error_messages={'invalid': 'Correo inválido.',
                        'required': 'Este campo es requerido.'}
    )
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'cuil': forms.TextInput(attrs={'maxlength': 11, 'class': 'finput'}),
            'nombre': forms.TextInput(attrs={'maxlength': 30, 'class': 'finput'}),
            'telefono': forms.TextInput(attrs={'maxlength': 12, 'class': 'finput'}),
            'email': forms.EmailInput(attrs={'class': 'finput'}),
            'domicilio': forms.TextInput(attrs={'maxlength': 50, 'class': 'finput'}),
            'edad': forms.TextInput(attrs={'class': 'finput'}),
            'lista': forms.CheckboxInput(attrs={'class': 'form-check-input'}), #modificacion de los checkbox
            'fotos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tall': forms.Select(attrs={'class': 'finput'}),
        }

        error_messages = {
            'nombre': {
                'required': 'Este campo es requerido',
            },
            'edad': {
                'required': 'Este campo es requerido',
            },
            'cuil': {
                'required': 'Este campo es requerido',
            },
            'domicilio': {
                'required': 'Este campo es requerido',
            },
            'telefono': {
                'required': 'Este campo es requerido',
            },
            'tall': {
                'required': 'Este campo es requerido',
            },
        }

    """def clean(self):
        cleaned_data = super().clean()
        required_fields = ['nombre', 'edad', 'cuil', 'domicilio', 'email', 'telefono']

        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, 'Este campo es requerido.')
        
        return cleaned_data"""

    def clean_cuil(self):
        cuil = self.cleaned_data.get('cuil')
        if not cuil.isdigit():
            raise forms.ValidationError('El CUIL debe contener solo números.')
        if not 8 <= len(cuil) <= 11:
            raise forms.ValidationError('El CUIL debe tener entre 8 y 11 dígitos.')
        return cuil
    
    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if not edad.isdigit():
            raise forms.ValidationError('La edad debe contener solo números.')
        return edad
        
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise forms.ValidationError('El teléfono debe contener solo números.')
        if not 8 <= len(telefono) <= 12:
            raise forms.ValidationError('El teléfono debe tener entre 8 y 12 dígitos.')
        return telefono
    
    # Definir el texto del placeholder para el campo 'tall'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tall'].empty_label = 'Seleccione taller'
