from django.db import models
from usuario.models import Profesor, Alumno

class Tesis(models.Model):
	"""
		Se registraran de las tesis: 
			* El tema y títulos de cada tesis
			* Los abstracs
			* Los nombres de los involucrados: alumno, directores y miembros del comite tutorial 
	"""

	nombreTesis= models.CharField(max_length= 100)
	alumno= models.ForeignKey(Alumno, on_delete= models.CASCADE, null=True)
	nombreTesis= models.CharField(max_length= 100)
	directores= models.ManyToManyField(Profesor)

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