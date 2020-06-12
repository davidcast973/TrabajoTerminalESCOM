from django.db import models
from usuario.models import Profesor

# Create your models here.
class ProgramaPosgrado(models.Model):
	"""
	    ProgramaPosgrado: Información sobre el programa de posgrado
	"""

	nombrePrograma = models.CharField(max_length=50)
	siglasPrograma = models.CharField(max_length=10)
	coordinadorPrograma = models.CharField(max_length= 200)
	semanasSemestrePrograma = models.IntegerField()

	class Meta:
		ordering = ['nombrePrograma']

	def __str__(self): 
		return self.nombrePrograma

class Laboratorio(models.Model):
	"""
	    Laboratorio: Información sobre los diferentes laboratorios
	"""

	nombreLaboratorio = models.CharField(max_length=100)
	jefeLaboratorio = models.CharField(max_length=200)

	class Meta:
		ordering = ['nombreLaboratorio']

	def __str__(self): 
		return self.nombreLaboratorio

class UnidadAprendizaje(models.Model):
	"""
	    Unidad de Aprendizaje: Información sobre las diferentes unidades de aprendizaje
	"""

	TIPO_UA_OPCION = dict(
		OBLIGATORIA = "Obligatoria",
		OPTATIVA = "Optativa"
		)
	TIPO_HORAS_UA_OPCION = dict(
		TEORIA = "Teoria",
		PRACTICA = "Practica",
		TEORICOPRACTICA = "Teorico-Practica",
		SEMINARIO = "Seminario",
		ESTANCIA = "Estancia"
		)
	nombreUA = models.CharField(max_length=200)
	tipoUA = models.CharField(
		max_length=15,
		choices=list(TIPO_UA_OPCION.items()),
	)
	tipoHorasUA = models.CharField(
		max_length=15,
		choices=list(TIPO_HORAS_UA_OPCION.items()),
	)
	horasSemanaUA = models.IntegerField()
	horasSemestreUA = models.IntegerField()
	creditosUA = models.DecimalField(max_digits= 4, decimal_places= 2)
	creditosSatcaUA = models.DecimalField(max_digits= 4, decimal_places= 2)

	class Meta:
		ordering = ['nombreUA']

	def __str__(self): 
		return self.nombreUA

class SituacionEscolar(models.Model):
	"""
	    SituacionEscolar: Guarda el registro de la situacion escolar de los alumnos
	"""

	usuario = models.ForeignKey('auth.User', on_delete= models.CASCADE, null=True)
	grupo = models.CharField(max_length=6)
	UA = models.ForeignKey(UnidadAprendizaje, on_delete= models.CASCADE)
	profesorUDA = models.ForeignKey(Profesor, on_delete= models.CASCADE)
	semestre = models.IntegerField()
	primerParcial = models.DecimalField(max_digits= 4, decimal_places= 2, blank=True, null=True)
	segundoParcial = models.DecimalField(max_digits= 4, decimal_places= 2, blank=True, null=True)
	tercerParcial = models.DecimalField(max_digits= 4, decimal_places= 2, blank=True, null=True)
	extraordinario = models.DecimalField(max_digits= 4, decimal_places= 2, blank=True, null=True)
	calificacionFinal = models.DecimalField(max_digits= 4, decimal_places= 2, blank=True, null=True)
	evaluacionProfesor = models.BooleanField()

	def __str__(self):
		return str(self.usuario)