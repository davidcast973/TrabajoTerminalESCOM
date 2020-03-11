from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(PersonalAdministrativo)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Permisos)