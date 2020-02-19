from django.shortcuts import render
from .models import *

# Create your views here.

def bosque_list(request):
	animales= Animal.objects.all().order_by('nombreAnimal')
	return render(request, 'bosque/bosque_list.html', {'animales': animales})