from django import forms
from .models import Socios



class SociosForm(forms.ModelForm):
    class Meta:
        model = Socios
        fields = ['nombreSocio', 'fechaIncorporacion', 'añoNacimiento', 'telefono', 'correo', 'estado', 'sexo', 'observacion']
        widgets = {
            'nombreSocio': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaIncorporacion': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'añoNacimiento': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
        }