from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(PersonalAdministrativo)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Permisos)