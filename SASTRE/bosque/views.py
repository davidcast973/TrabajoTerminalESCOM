from django.shortcuts import render
from .models import *

# Create your views here.

def animal_list(request):
	animales= Animal.objects.all().order_by('nombreAnimal')
	return render(request, 'bosque/animal_list.html', {'animales': animales})

def planta_list(request):
	plantas= Planta.objects.all().order_by('nombreFruto')
	return render(request, 'bosque/planta_list.html', {'plantas': plantas})