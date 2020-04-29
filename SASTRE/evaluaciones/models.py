from django.db import models

# Create your models here.

class Materia(models.Model):
	"""
	    Materias: Inicialmente servirá para mostrar las materías que ha cursado
	"""

	nombreMateria= models.CharField(max_length=50)

	class Meta:
		ordering = ['nombreMateria']

	def __str__(self): 
		return self.nombreMateria

class Pregunta(models.Model):
	"""
		Preguntas para agregar a cuestionarios
	"""
	textoPregunta= models.CharField(max_length=200)

	def __str__(self):
		return str(self.textoPregunta)

class Cuestionario(models.Model):
	"""
		Un modelo que guardarálos cuestionarios disponibles
	"""
	RESPUESTA_OPCION= dict(R1= '1', R2= '2', R3= '3', R4= '4', R5='5')
	usuario= models.ForeignKey('auth.User', on_delete= models.CASCADE, null=True)
	bandera = models.BooleanField()
	r1= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r2= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r3= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r4= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r5= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r6= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r7= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r8= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r9= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r10= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r11= models.CharField(
		max_length=1,
		choices=list(RESPUESTA_OPCION.items()),
	)
	r12= models.TextField()
	

	def __str__(self):
		return str(self.titulo)