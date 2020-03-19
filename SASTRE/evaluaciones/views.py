from django.shortcuts import render

# Create your views here.

def evaluarProfesor(request):
    return render(request, 'evaluarProfesor.html')

def materiasCursadas(request):
    return render(request, 'listadoMaterias.html')
