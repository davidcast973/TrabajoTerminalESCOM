from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from inscripcionTesis.views import *

urlpatterns = [
    path('profesor/', views.evaluarProfesor, name='evaluarProfesor'),
    path('materias/', views.materiasCursadas, name='materiasCursadas'),
    path('etiquetar/', views.etiquetadoTexto, name='etiquetadoTexto'),
]