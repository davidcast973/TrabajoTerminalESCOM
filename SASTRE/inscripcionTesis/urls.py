from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from inscripcionTesis.views import *

urlpatterns = [
    path('vizualizarTesis', views.vertesis, name='vertesis'),
    path('inscripcionTesis', views.inscripcionTesisInicio, name='inscripcionTesisInicio'),
    path('tesisSimilares', views.tesisSimilares, name='tesisSimilares'),
    path('omitirProfesor', views.omitirProfesor, name='omitirProfesor'),
    path('seleccionarDirector1', views.seleccionarDirector1, name='seleccionarDirector1'),
    path('seleccionarDirector2', views.seleccionarDirector2, name='seleccionarDirector2'),
    path('seleccionarCT1', views.seleccionarCT1, name='seleccionarCT1'),
    path('seleccionarCT2', views.seleccionarCT2, name='seleccionarCT2'),
    path('seleccionarCT3', views.seleccionarCT3, name='seleccionarCT3'),
    path('seleccionarCT4', views.seleccionarCT4, name='seleccionarCT4'),
    path('registrarTesis', views.registrarTesis, name='registrarTesis'),
    path('guardarTesis', views.guardarTesis, name='guardarTesis'),
]