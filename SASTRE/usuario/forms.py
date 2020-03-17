from django import forms
from .models import *

# NACIONALIDAD = [(x.nombrePermiso,x.nombrePermiso) for x in Permisos.objects.all()]
# 
# NACIONALIDADD = [
# 	('mexicano','mexicano'),
# 	('aleman','aleman'),
# 	('frances','frances'),
# 	('chileno','chileno'),
# 	('español','español'),
# ]

class UsuarioForm(forms.ModelForm):

	fechaNacimiento = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = Usuario
		fields = '__all__'

class PersonalAdminForm(forms.ModelForm):

	fechaNacimiento = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = PersonalAdministrativo
		fields = '__all__'

class ProfesorForm(forms.ModelForm):

	fechaNacimiento = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = Profesor
		fields = '__all__'

class AlumnoForm(forms.ModelForm):

	fechaNacimiento = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = Alumno
		fields = '__all__'