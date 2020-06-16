from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from inscripcionTesis.views import *

urlpatterns = [
    path('inscripcionTesis', inscripcionTesisInicio.as_view(), name='inscripcionTesisInicio'),
    path('vizualizarTesis', vertesis.as_view(), name='vertesis'),
]