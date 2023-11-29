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
    def clean_nombreSocio(self):
            nom = self.cleaned_data['nombreSocio']
            if len(nom) >= 80:
                raise forms.ValidationError("El largo máximo del nombre son 80 caracteres.")
            return nom
    
    def clean_telefono(self):
            fono = self.cleaned_data['telefono']
            if len(fono) <= 9 and len(fono) >=13 :
                raise forms.ValidationError("El largo minimo del celular es 9 y el maximo 12.")
            return fono