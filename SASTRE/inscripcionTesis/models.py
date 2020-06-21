from django.db import models
from usuario.models import Profesor, Alumno

class Tesis(models.Model):
	"""
		Se registraran de las tesis: 
			* El tema y títulos de cada tesis
			* Los abstracs
			* Los nombres de los involucrados: alumno, directores y miembros del comite tutorial 
	"""

	numeroTesis= models.IntegerField(default=0)
	nombreTesis= models.CharField("Titulo de la tesis", max_length= 500, default= "")
	alumnoAps= models.CharField("Apeido(s) del alumno autor", max_length= 100, default= "")
	alumno= models.CharField("Nombre del alumno autor", max_length= 100, default= "")
	director1Aps= models.CharField("Apeido(s) de director 1", max_length=50, default= "")
	director1= models.CharField("Nombre de director 1", max_length=50, default= "")
	director2Aps= models.CharField("Apeido(s) de director 1", max_length=50, default= "")
	director2= models.CharField("Nombre de director 1", max_length=50, default= "")
	abstrac= models.TextField("Abstrac de la tesis", default= "", null=True)
	diaCreacion= models.DateField(default='1920-01-01', null=True)
	valorW2V= models.TextField("Valor obtenido de word2vec", default= ','.join([str(0) for x in range(300)]), null=True)

	def __str__(self):
		return str(self.nombreTesis)

class ComiteTutorial(models.Model):
	"""
		Se pone en una clase aparte el comite para que pueda generarse el campo ManyToMany.
		El vinculo con la tesis es buscando la tesis por su nombre.
	"""

	tesis= models.ForeignKey(Tesis, on_delete= models.CASCADE, null=True)
	miembros= models.ManyToManyField(Profesor)

	def __str__(self):
		return str(self.tesis)