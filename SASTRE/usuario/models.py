from django.db import models

# Create your models here.

class Usuario(models.Model):
	"""
		docstring for usuario: Clase que describe al objeto usuario.
	"""

	usuario= models.ForeignKey('auth.User', on_delete= models.CASCADE)
	edad= models.IntegerField()
	direccion= models.CharField(max_length= 200)
	lada= models.CharField(max_length= 4)
	telefono= models.CharField(max_length= 10)
	curp= models.CharField(max_length= 18)

	def ingresarAlSistema(self):
		pass
		
class PersonalAdministravito(Usuario):
	"""
		docstring for PersonalAdministravito
	"""
	numEmpleado= models.IntegerField()
	departamento= models.CharField(max_length= 50)
	
		
class Profesor(Usuario):
	"""docstring for Profesor"""
		
class Alumno(Usuario):
	"""docstring for Alumno"""
		