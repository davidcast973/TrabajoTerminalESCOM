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

	#fechaNacimiento = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = Usuario
		fields = '__all__'
		#exclude = ['fechaNacimiento']
		widgets = {
            'fechaNacimiento': forms.DateInput(attrs={'class':'datepicker'}),
        }

class PersonalAdminForm(forms.ModelForm):

	#fechaNacimiento = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = PersonalAdministrativo
		fields = '__all__'
		#exclude = ['fechaNacimiento']
		widgets = {
            'fechaNacimiento': forms.DateInput(attrs={'class':'datepicker'}),
        }

class ProfesorForm(forms.ModelForm):

	fechaNacimiento = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = Profesor
		fields = '__all__'
		exclude = ['fechaNacimiento']

class AlumnoForm(forms.ModelForm):

	fechaNacimiento = forms.DateField(widget=forms.SelectDateWidget())
	class Meta:
		model = Alumno
		fields = '__all__'
		exclude = ['fechaNacimiento']