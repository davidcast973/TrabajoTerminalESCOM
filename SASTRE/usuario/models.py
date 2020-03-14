from django.db import models

# Create your models here.

class Usuario(models.Model):
	"""
		docstring for usuario: Clase que describe al objeto usuario.
		Nesesario aclarar diferencia entre cuenta y usuario
	"""
	ALEMANIA = 'AL'
	BRASIL = 'BR'
	CANADA = 'CA'
	DINAMARCA = 'DI'
	ECUADOR = 'EC'
	MEXICO = 'MX'
	PAIS_CHOICES = [
		(ALEMANIA, 'Alemania'),
		(BRASIL, 'Brasil'),
		(CANADA, 'Canada'),
		(DINAMARCA, 'Dinamarca'),
		(ECUADOR, 'Ecuador'),
		(MEXICO, 'Mexico'),
	]

	nombreUsuario= models.ForeignKey('auth.User', on_delete= models.CASCADE)
	edad= models.IntegerField()
	direccion= models.CharField(max_length= 200)
	lada= models.CharField(max_length= 4)
	telefono= models.CharField(max_length= 10)
	curp= models.CharField(max_length= 18)
	fechaNacimiento = models.DateField()
	paisNacimiento = models.CharField(
		max_length=2,
		choices=PAIS_CHOICES,
		default=MEXICO,
	)

	def __str__(self):
		return str(self.nombreUsuario)
			
class PersonalAdministrativo(Usuario):
	"""
		docstring for PersonalAdministrativo:
	"""
	numEmpleado= models.IntegerField()
	departamento= models.CharField(max_length= 50)

	def __str__(self):
		return str(self.nombreUsuario)

class Profesor(Usuario):
	"""
		docstring for Profesor: 
	"""

	tiraMaterias= models.TextField()
	titulo= models.FileField(upload_to=None, max_length=100)
	cedula= models.CharField(max_length= 20)
	numEmpleado= models.IntegerField()

	def __str__(self):
		return str(self.nombreUsuario)

		
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

	def __str__(self):
		return str(self.nombreUsuario)

class Permisos(models.Model):
	"""docstring for ClassName"""
	nombrePermiso = models.CharField(max_length=30)
	descripcion = models.TextField()
	charAllllint = models.CharField(max_length=10, blank=True, null=True)
	numeroBlank = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.nombrePermiso