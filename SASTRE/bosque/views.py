from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def animal_list(request):
	animales= Animal.objects.all().order_by('nombreAnimal')
	return render(request, 'bosque/animal_list.html', {'animales': animales})

def planta_list(request):
	plantas= Planta.objects.all().order_by('nombreFruto')
	return render(request, 'bosque/planta_list.html', {'plantas': plantas})

def faunas_list(request):
	faunas= Fauna.objects.all().order_by('nombreFauna')
	return render(request, 'bosque/faunas_list.html', {'faunas': faunas})

def animal_detalle(request, pk):
	animal = get_object_or_404(Animal, pk=pk)
	return render(request, 'bosque/animal_detalle.html', {'animal': animal})

def fauna_detalle(request, pk):
	fauna = get_object_or_404(Fauna, pk=pk)
	return render(request, 'bosque/fauna_detalle.html', {'fauna': fauna})