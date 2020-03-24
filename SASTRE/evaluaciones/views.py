from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/cuenta/login/')
def evaluarProfesor(request):
    return render(request, 'evaluarProfesor.html')

@login_required(login_url='/cuenta/login/')
def materiasCursadas(request):
    return render(request, 'listadoMaterias.html')
