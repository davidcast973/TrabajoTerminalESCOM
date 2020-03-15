from django.shortcuts import render, get_object_or_404
from .forms import *
from django.shortcuts import redirect
from .models import Usuario, PersonalAdministrativo, Profesor, Alumno
from django.contrib.auth.models import User

def bienvenida(request):
    usuario= Usuario.objects.get(nombreUsuario= request.user)
    return render(request, 'bienvenida.html', {'usuario': usuario})

def usuario_new(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario.save()
            return redirect('usuario_detail', pk=usuario.pk)
    else:
        form = UsuarioForm()
    return render(request, 'usuario/usuario_edit.html', {'form': form})

def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save()
            usuario.save()
            return redirect('usuario_detail', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/usuario_edit.html', {'form': form})

def usuario_detail(request, pk):
	usuario = get_object_or_404(Usuario, pk=pk)
	return render(request, 'usuario/usuario_detail.html', {'usuario': usuario})

def crudInicio(request):
    mensaje = "Prueba"
    if request.method == "POST":
        formPA = PersonalAdminForm(request.POST)
        formProf = ProfesorForm(request.POST)
        formAlum = AlumnoForm(request.POST)
        if request.POST.get("save_pa"):
            if formPA.is_valid():
                pa = formPA.save()
                pa.save()
                mensaje = "Se genero exitosamente una cuenta para personal administrativo"
                return render(request, 'crud/crudInicio.html', {'formPA': formPA, 'formProf': formProf, 'formAlum': formAlum, 'mensaje': mensaje})
        elif request.POST.get("save_profesor"):
            if formProf.is_valid():
                profesor = formProf.save()
                profesor.save()
                mensaje = "Se genero exitosamente una cuenta para un profesor"
                return render(request, 'crud/crudInicio.html', {'formPA': formPA, 'formProf': formProf, 'formAlum': formAlum, 'mensaje': mensaje})
        elif request.POST.get("save_alumno"):
            if formAlum.is_valid():
                alumno = formAlum.save()
                alumno.save()
                mensaje = "Se genero exitosamente una cuenta para un alumno"
                return render(request, 'crud/crudInicio.html', {'formPA': formPA, 'formProf': formProf, 'formAlum': formAlum, 'mensaje': mensaje})
    else:
        formPA = PersonalAdminForm()
        formProf = ProfesorForm()
        formAlum = AlumnoForm()
    return render(request, 'crud/crudInicio.html', {'formPA': formPA, 'formProf': formProf, 'formAlum': formAlum, 'mensaje': mensaje})