from django.http import HttpResponse
from django.shortcuts import render
from controlSesion.forms import LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("Inicio de sesion")

def login_page(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Has iniciado sesion correctamente"
				else:
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = LoginForm()
	return render(request, 'controlSesion/login.html', {'message':message, 'form':form})