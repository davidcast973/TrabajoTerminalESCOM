from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from inscripcionTesis.views import *

urlpatterns = [
	path('evaluarProfesores/', views.evaluacionProfesorInicio, name='evaluacionProfesorInicio'),
    path('evaluarProfesores/evaluarProfesor/', views.evaluarProfesor, name='evaluarProfesor'),
    path('materias/', views.materiasCursadas, name='materiasCursadas'),
    path('etiquetar/', views.etiquetadoTexto, name='etiquetadoTexto'),
    path('guardarEvaluacion/', views.guardarEvaluacion, name='guardarEvaluacion'),
    path('resultadoEvaluaciones/', views.resultadoEvaluacionesInicio, name='resultadoEvaluacionesInicio'),
    path('resultadoEvaluaciones/evaluacionDetalle', views.evaluacionDetalle, name='evaluacionDetalle'),
]