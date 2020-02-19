from django.shortcuts import render, get_object_or_404
from .forms import UsuarioForm
from django.shortcuts import redirect
from .models import Usuario, PersonalAdministrativo, Profesor, Alumno

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
    return render(request, 'usuario/usuario_detail.html', {'post': usuario})