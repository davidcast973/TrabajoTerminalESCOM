"""sastre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import *

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html')),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('tesis/', include('inscripcionTesis.urls')),
    path('evaluaciones/', include('evaluaciones.urls')),

    # Add Django site authentication urls (for login, logout, password management)
    # path('cuenta/', include('django.contrib.auth.urls')),
    # Con estos ya podemos tener acceso a los atributos de las vistas, por lo cual podemos enviar los correos electronicos.
    url(r'^cuenta/login/$', LoginView.as_view(), {'template_name': 'registration/login.html'}, name= 'login'),
    url(r'^cuenta/logout/$', LogoutView.as_view(), {'template_name': 'registration/login.html'}, name= 'logout'),
    url(r'^cuenta/password_reset/$', PasswordResetView.as_view(), {'template_name': 'registration/password_reset_form.html', 'email_template_name': 'registration/password_reset_email.html'}, name= 'password_reset'),
    url(r'^cuenta/password_reset_done/$', PasswordResetDoneView.as_view(), {'template_name': 'registration/password_reset_done.html'}, name= 'password_reset_done'),
    url(r'^cuenta/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), {'template_name': 'registration/password_reset_confirm.html'}, name= 'password_reset_confirm'),
    url(r'^cuenta/password_reset_complete/$', PasswordResetCompleteView.as_view(), {'template_name': 'registration/password_reset_complete.html'}, name= 'password_reset_complete'),
]

admin.site.site_header = 'Administrador del sistema SASTRE'