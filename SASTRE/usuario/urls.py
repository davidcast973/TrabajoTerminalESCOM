from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from usuario.views import *

urlpatterns = [
    path('bienvenida/', views.bienvenida, name='bienvenida'),
	path('crud/', views.crudInicio, name='crudInicio'),

    # La ruta 'crudPA' en donde listamos todos los registros de la Base de Datos
    path('adminPA/', PAListado.as_view(template_name = "adminPA/index.html"), name='crudPA'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un PA
    path('adminPA/detalle/<int:pk>', PADetalle.as_view(template_name = "adminPA/detalles.html"), name='detalles'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo PA
    path('adminPA/crear', PACrear.as_view(template_name = "adminPA/crear.html"), name='crear'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un PA
    path('adminPA/editar/<int:pk>', PAActualizar.as_view(template_name = "adminPA/actualizar.html"), name='actualizar'), 
    # La ruta 'eliminar' que usaremos para eliminar un PA
    path('adminPA/eliminar/<int:pk>', PAEliminar.as_view(), name='eliminar'),

    # La ruta 'crudProfesor' en donde listamos todos los registros de la Base de Datos
    path('adminProfesor/', ProfesorListado.as_view(template_name = "adminProfesor/index.html"), name='crudProfesor'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un PA
    path('adminProfesor/detalle/<int:pk>', ProfesorDetalle.as_view(template_name = "adminProfesor/detalles.html"), name='detalles'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo PA
    path('adminProfesor/crear', ProfesorCrear.as_view(template_name = "adminProfesor/crear.html"), name='crear'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un PA
    path('adminProfesor/editar/<int:pk>', ProfesorActualizar.as_view(template_name = "adminProfesor/actualizar.html"), name='actualizar'), 
    # La ruta 'eliminar' que usaremos para eliminar un PA
    path('adminProfesor/eliminar/<int:pk>', ProfesorEliminar.as_view(), name='eliminar'),

    # La ruta 'crudAlumno' en donde listamos todos los registros de la Base de Datos
    path('adminAlumno/', AlumnoListado.as_view(template_name = "adminAlumno/index.html"), name='crudAlumno'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un PA
    path('adminAlumno/detalle/<int:pk>', AlumnoDetalle.as_view(template_name = "adminAlumno/detalles.html"), name='detalles'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo PA
    path('adminAlumno/crear', AlumnoCrear.as_view(template_name = "adminAlumno/crear.html"), name='crear'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un PA
    path('adminAlumno/editar/<int:pk>', AlumnoActualizar.as_view(template_name = "adminAlumno/actualizar.html"), name='actualizar'), 
    # La ruta 'eliminar' que usaremos para eliminar un PA
    path('adminAlumno/eliminar/<int:pk>', AlumnoEliminar.as_view(), name='eliminar'),
]