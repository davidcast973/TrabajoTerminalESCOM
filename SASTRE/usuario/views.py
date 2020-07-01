from django.shortcuts import render, get_object_or_404
from .forms import *
from django.shortcuts import redirect
from .models import Usuario, PersonalAdministrativo, Profesor, Alumno
from django.contrib.auth.models import User
# Habilitamos el uso de mensajes en Django
from django.contrib import messages
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin  
# Habilitamos los formularios en Django
from django import forms
from django.contrib.auth.decorators import login_required

@login_required(login_url='/cuenta/login/')
def bienvenida(request):
    usuario= Usuario.objects.get(username= request.user)
    bandera = 1
    if (Alumno.objects.filter(username= request.user).count()) > 0:
        bandera = 1
    elif (Profesor.objects.filter(username= request.user).count()) > 0:
        bandera = 2
    elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
        bandera = 3
    return render(request, 'bienvenida.html', {'usuario': usuario, 'tipoUsuario': bandera})

@login_required(login_url='/cuenta/login/')
def crudInicio(request):
    mensaje = "Prueba"
    formPA = PersonalAdminForm()
    formProf = ProfesorForm()
    formAlum = AlumnoForm()
    bandera = 1
    if (Alumno.objects.filter(username= request.user).count()) > 0:
        bandera = 1
    elif (Profesor.objects.filter(username= request.user).count()) > 0:
        bandera = 2
    elif (PersonalAdministrativo.objects.filter(username= request.user).count()) > 0:
        bandera = 3
    return render(request, 'crud/crudInicio.html', {'formPA': formPA, 'formProf': formProf, 'formAlum': formAlum, 'mensaje': mensaje, 'tipoUsuario': bandera})

#=======================   CRUD Personal Administrativo   =======================#
class PAListado(ListView): 
    model = PersonalAdministrativo
 
class PADetalle(DetailView): 
    model = PersonalAdministrativo
 
class PACrear(SuccessMessageMixin, CreateView): 
    model = PersonalAdministrativo
    form = PersonalAdministrativo
    fields = "__all__"
    success_message = '¡Personal Administrativo creado correctamente!' # Mostramos este Mensaje luego de crear un personal administrativo     
    
    
    def form_valid(self, form):
        user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
        )
        user.last_name = form.cleaned_data['nombre']
        user.first_name = form.cleaned_data['apellido']
        user.save()
        return super().form_valid(form)
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('crudPA') # Redireccionamos a la vista principal 'crudPA' 
 
class PAActualizar(SuccessMessageMixin, UpdateView): 
    model = PersonalAdministrativo
    form = PersonalAdministrativo
    fields = "__all__" 
    success_message = '!Personal Administrativo actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Personal Administrativo 
    
    def form_valid(self, form):
        u = User.objects.get(username=form.cleaned_data['username'])
        u.set_password(form.cleaned_data['password'])
        u.last_name = form.cleaned_data['nombre']
        u.first_name = form.cleaned_data['apellido']
        u.save()
        return super().form_valid(form)
    # Redireccionamos a la página principal luego de actualizar un registro o Personal Administrativo
    def get_success_url(self):               
        return reverse('crudPA') # Redireccionamos a la vista principal 'crudPA' 
 
class PAEliminar(SuccessMessageMixin, DeleteView): 
    model = PersonalAdministrativo
    form = PersonalAdministrativo
    fields = "__all__"
 
    # Redireccionamos a la página principal luego de eliminar un registro o Personal Administrativo
    def get_success_url(self): 
        success_message = '!Personal Administrativo eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Personal Administrativo 
        messages.success (self.request, (success_message))       
        return reverse('crudPA') # Redireccionamos a la vista principal 'crudPA'

#=======================   CRUD Profesores   =======================#
class ProfesorListado(ListView): 
    model = Profesor
 
class ProfesorDetalle(DetailView): 
    model = Profesor
 
class ProfesorCrear(SuccessMessageMixin, CreateView): 
    model = Profesor
    form = Profesor
    fields = "__all__"
    success_message = '!Profesor creado correctamente!' # Mostramos este Mensaje luego de crear un profesor
    
    def form_valid(self, form):
        user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
        )
        user.last_name = form.cleaned_data['nombre']
        user.first_name = form.cleaned_data['apellido']
        user.save()
        return super().form_valid(form)
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('crudProfesor') # Redireccionamos a la vista principal 'crudProfesor' 
 
class ProfesorActualizar(SuccessMessageMixin, UpdateView): 
    model = Profesor
    form = Profesor
    fields = "__all__" 
    success_message = '!Profesor actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Profesor 

    def form_valid(self, form):
        uProf = User.objects.get(username=form.cleaned_data['username'])
        uProf.set_password(form.cleaned_data['password'])
        uProf.last_name = form.cleaned_data['nombre']
        uProf.first_name = form.cleaned_data['apellido']
        uProf.save()
        return super().form_valid(form)
    # Redireccionamos a la página principal luego de actualizar un registro o Profesor
    def get_success_url(self):               
        return reverse('crudProfesor') # Redireccionamos a la vista principal 'crudProfesor' 
 
class ProfesorEliminar(SuccessMessageMixin, DeleteView): 
    model = Profesor
    form = Profesor
    fields = "__all__"
 
    # Redireccionamos a la página principal luego de eliminar un registro o Profesor
    def get_success_url(self): 
        success_message = '!Profesor eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Profesor 
        messages.success (self.request, (success_message))       
        return reverse('crudProfesor') # Redireccionamos a la vista principal 'crudProfesor'

#=======================   CRUD Alumnos   =======================#
class AlumnoListado(ListView): 
    model = Alumno
 
class AlumnoDetalle(DetailView): 
    model = Alumno
 
class AlumnoCrear(SuccessMessageMixin, CreateView): 
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = '!Alumno creado correctamente!' # Mostramos este Mensaje luego de crear un Alumno     
    
    def form_valid(self, form):
        user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
        )
        user.last_name = form.cleaned_data['nombre']
        user.first_name = form.cleaned_data['apellido']
        user.save()
        return super().form_valid(form)
    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):
        return reverse('crudAlumno') # Redireccionamos a la vista principal 'crudAlumno' 
 
class AlumnoActualizar(SuccessMessageMixin, UpdateView): 
    model = Alumno
    form = Alumno
    fields = "__all__" 
    success_message = '!Alumno actualizado correctamente!' # Mostramos este Mensaje luego de Editar un Alumno 

    def form_valid(self, form):
        u = User.objects.get(username=form.cleaned_data['username'])
        u.set_password(form.cleaned_data['password'])
        u.last_name = form.cleaned_data['nombre']
        u.first_name = form.cleaned_data['apellido']
        u.save()
        return super().form_valid(form)
    # Redireccionamos a la página principal luego de actualizar un registro o Alumno
    def get_success_url(self):               
        return reverse('crudAlumno') # Redireccionamos a la vista principal 'crudAlumno' 
 
class AlumnoEliminar(SuccessMessageMixin, DeleteView): 
    model = Alumno
    form = Alumno
    fields = "__all__"
 
    # Redireccionamos a la página principal luego de eliminar un registro o Alumno
    def get_success_url(self): 
        success_message = '!Alumno eliminado correctamente!' # Mostramos este Mensaje luego de Editar un Alumno 
        messages.success (self.request, (success_message))       
        return reverse('crudAlumno') # Redireccionamos a la vista principal 'crudAlumno'