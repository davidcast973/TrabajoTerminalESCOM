from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views import View

class inscripcionTesisInicio(View):
	template_name = "tesis/inscripcionTesisInicio.html"
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		return render(request, self.template_name)

class vertesis(View):
	template_name = "tesis/vertesis.html"
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		return render(request, self.template_name)