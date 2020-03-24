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
