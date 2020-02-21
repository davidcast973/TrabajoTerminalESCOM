from django.forms import *

from .models import Usuario, Profesor, Alumno, PersonalAdministrativo

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ('nombreUsuario', 'edad', 'direccion', 'lada', 'telefono', 'curp')
        widgets = {
        	'nombreUsuario': TextInput(attrs={'class': 'form-control'})
        }