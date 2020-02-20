from django.db import models

# Create your models here.

class Usuario(models.Model):
	"""
		docstring for usuario: Clase que describe al objeto usuario.
		Nesesario aclarar diferencia entre cuenta y usuario
	"""

	nombreUsuario= models.ForeignKey('auth.User', on_delete= models.CASCADE)
	edad= models.IntegerField()
	direccion= models.CharField(max_length= 200)
	lada= models.CharField(max_length= 4)
	telefono= models.CharField(max_length= 10)
	curp= models.CharField(max_length= 18)

	def __str__(self):
		return str(self.nombreUsuario)
			
class PersonalAdministrativo(Usuario):
	"""
		docstring for PersonalAdministrativo:
	"""
	numEmpleado= models.IntegerField()
	departamento= models.CharField(max_length= 50)

	def __str__(self):
		return self.numEmpleado

class Profesor(Usuario):
	"""
		docstring for Profesor: 
	"""

	tiraMaterias= models.TextField()
	titulo= models.FileField(upload_to=None, max_length=100)
	cedula= models.CharField(max_length= 20)
	numEmpleado= models.IntegerField()
		
class Alumno(Usuario):
	"""
		docstring for Alumno: 
	"""

	numRegistro= models.CharField(max_length= 20)
	modalidad= models.BooleanField()
	programa= models.CharField(max_length= 20)
	beca= models.IntegerField()
	ingles= models.BooleanField()
	cedula= models.CharField(max_length= 20)
	calfEXADEP= models.IntegerField()
	calfGRE= models.IntegerField()
	promedio= models.DecimalField(max_digits= 4, decimal_places= 2)
	escuelaLic= models.CharField(max_length= 100)
	lugarLic= models.CharField(max_length= 100)
	carrera= models.CharField(max_length= 50)
	titulo= models.TextField()
	entrevista= models.CharField(max_length= 20)