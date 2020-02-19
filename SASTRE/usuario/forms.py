from django import forms

from .models import Usuario, Profesor, Alumno, PersonalAdministrativo

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('usuario', 'edad', 'direccion', 'lada', 'telefono', 'curp')