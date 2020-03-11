from django import forms
from .models import *

NACIONALIDAD = [(x.nombrePermiso,x.nombrePermiso) for x in Permisos.objects.all()]

NACIONALIDADD = [
	('mexicano','mexicano'),
	('aleman','aleman'),
	('frances','frances'),
	('chileno','chileno'),
	('español','español'),
]

class UsuarioForm(forms.ModelForm):

    fechaNacimiento= forms.DateField(widget=forms.SelectDateWidget())
    nacionalidad = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=NACIONALIDAD,
    )
    class Meta:
        model = Usuario
        fields = ('nombreUsuario', 'edad', 'direccion', 'lada', 'telefono', 'curp')
        