from django.db import models

# Create your models here.

class Animal(models.Model):
	"""docstring for Animal: Esta clase describe a cada animal que se en cuentra en un determinado bosque."""
	
	nombreAnimal= models.CharField(max_length= 20)
	garras= models.BooleanField()
	alas= models.BooleanField()
	plumas= models.BooleanField()
	cola= models.BooleanField()

	def __str__(self):
		return self.nombreAnimal

class Planta(models.Model):
	"""docstring for Animal: Esta clase describe a cada animal que se en cuentra en un determinado bosque."""
	
	nombrePlanta= models.CharField(max_length= 20, default= 'Manzana')
	frutos= models.BooleanField()
	nombreFruto= models.CharField(max_length= 20, blank= True)

	def __str__(self):
		return self.nombrePlanta