from django.db import models
from usuario.models import Profesor, Alumno

class Tesis(models.Model):
	"""
		Se registraran de las tesis: 
			* El tema y títulos de cada tesis
			* Los abstracs
			* Los nombres de los involucrados: alumno, directores y miembros del comite tutorial 
	"""

	idTesis= models.AutoField(primary_key=True)
	nombreTesis= models.CharField("Titulo de la tesis",max_length= 500, default= "")
	alumno= models.CharField("Nombre del alumno autor",max_length= 100, default= "")
	abstrac= models.CharField("Abstrac de la tesis",max_length=5000, default= "")
	director1= models.CharField("Ingresar nombre de director 1", max_length=50, default= "")
	director2= models.CharField("Ingresar nombre de director 2", max_length=50, default= "")

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