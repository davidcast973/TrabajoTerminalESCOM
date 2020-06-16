from django.db import models

PAIS_OPCION= dict(
	ALEMANIA= 'Alemania',
	BRASIL= 'Brasil',
	CANADA= 'Canada',
	DINAMARCA= 'Dinamarca',
	ECUADOR= 'Ecuador',
	MEXICO= 'Mexico',
)

GENERO_OPCION= dict(F= 'Femenino', M= 'Masculio',)

class Usuario(models.Model):
	"""
		docstring for usuario: Clase que describe al objeto usuario.
		Nesesario aclarar diferencia entre cuenta y usuario
	"""

	#nombreUsuario= models.ForeignKey('auth.User', on_delete= models.CASCADE, null=True)
	username = models.CharField(max_length= 10)
	password = models.CharField(max_length= 100)
	email = models.CharField(max_length = 100)
	nombre = models.CharField(max_length= 200)
	apellido = models.CharField(max_length= 200)
	edad= models.IntegerField()
	direccion= models.CharField(max_length= 200)
	lada= models.CharField(max_length= 4)
	telefono= models.CharField(max_length= 10)
	curp= models.CharField(max_length= 18)
	fechaNacimiento= models.DateField()
	paisNacimiento= models.CharField(
		max_length=20,
		choices=list(PAIS_OPCION.items()),
		default='MEXICO',
	)
	genero= models.CharField(
		max_length=1,
		choices=list(GENERO_OPCION.items()),
	)
	identificador= models.CharField(max_length= 10)

	def __str__(self):
		return str(self.username)
			
class PersonalAdministrativo(Usuario):
	"""
		docstring for PersonalAdministrativo:
	"""
	departamento= models.CharField(max_length= 50)

	def __str__(self):
		return str(self.username)

class Profesor(Usuario):
	"""
		docstring for Profesor: 
	"""

	#materias= models.ManyToManyField(Materia)
	#titulo= models.FileField(upload_to='uploads/', max_length=100)
	cedula= models.CharField(max_length= 20)

	def __str__(self):
		return str(self.username)
		
class Alumno(Usuario):
	"""
		docstring for Alumno: 
	"""
	BECA_OPCION = [
		('INSTITUCIONAL_ESTUDIO', 'Institucional Estudio'),
		('INSTITUCIONAL_TESIS', 'Institucional Tesis'),
		('TRANSPORTE', 'Transporte'),
		('BEIFI', 'BEIFI'),
		('EXCELENCIA', 'Excelencia'),
	]

	modalidad= models.BooleanField()
	programa= models.CharField(max_length= 50)
	beca = models.CharField(
		max_length=20,
		choices=BECA_OPCION,
		default='1',
	)
	ingles= models.BooleanField()
	cedula= models.CharField(max_length= 20)
	calfEXADEP= models.IntegerField()
	calfGRE= models.IntegerField()
	promedio= models.DecimalField(max_digits= 4, decimal_places= 2)
	escuelaLic= models.CharField(max_length= 100)
	lugarLic= models.CharField(max_length= 100)
	carrera= models.CharField(max_length= 50)
	#titulo= models.TextField()
	entrevista= models.CharField(max_length= 20)

	def __str__(self):
		return str(self.username)

class Permisos(models.Model):
	"""docstring for ClassName"""
	nombrePermiso = models.CharField(max_length=30)
	descripcion = models.TextField()
	charAllllint = models.CharField(max_length=10, blank=True, null=True)
	numeroBlank = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.nombrePermiso