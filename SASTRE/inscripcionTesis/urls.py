from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from inscripcionTesis.views import *

urlpatterns = [
    path('', inscripcionTesisInicio.as_view(), name='inscripcionTesisInicio'),
]