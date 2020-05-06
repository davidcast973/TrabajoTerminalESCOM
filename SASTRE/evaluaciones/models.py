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

class CuestionarioManager(models.Manager):
    def create_cuestionario(self, usuario, bandera, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12):
        cuestionario = self.create(usuario=usuario, bandera=bandera, r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, r6=r6, r7=r7, r8=r8, r9=r9, r10=r10, r11=r11, r12=r12)
        # do something with the cuestionario
        return cuestionario

class Cuestionario(models.Model):
	"""
		Un modelo que guardarálos cuestionarios disponibles
	"""
	RESPUESTA_OPCION= dict(R1= '1', R2= '2', R3= '3', R4= '4', R5='5')
	usuario= models.ForeignKey('auth.User', on_delete= models.CASCADE, null=True)
	bandera = models.BooleanField()
	r1= models.CharField(
		max_length=2
	)
	r2= models.CharField(
		max_length=2
	)
	r3= models.CharField(
		max_length=2
	)
	r4= models.CharField(
		max_length=2
	)
	r5= models.CharField(
		max_length=2
	)
	r6= models.CharField(
		max_length=2
	)
	r7= models.CharField(
		max_length=2
	)
	r8= models.CharField(
		max_length=2
	)
	r9= models.CharField(
		max_length=2
	)
	r10= models.CharField(
		max_length=2
	)
	r11= models.CharField(
		max_length=2
	)
	r12= models.TextField()
	objects = CuestionarioManager()

	def __str__(self):
		return str(self.bandera)