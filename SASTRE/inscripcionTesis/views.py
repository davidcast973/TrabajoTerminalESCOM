from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views import View
from .models import *

def vertesis(request):
	allTesis= Tesis.objects.all().order_by('-numeroTesis')
	numAllTesis= len(allTesis)
	cantPag= list(range(1,(numAllTesis//18)+1))
	modPag= list(range(1,(numAllTesis%18)+1))

	return render(request, 'tesis/vertesis.html', {'allTesis': allTesis, 'numAllTesis':numAllTesis, 'cantPag':cantPag, 'modPag':modPag,})

class inscripcionTesisInicio(View):
	template_name = "tesis/inscripcionTesisInicio.html"
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		return render(request, self.template_name)