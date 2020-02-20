from django.urls import path
from . import views

app_name = 'controlSesion'
urlpatterns = [
    path('', views.index, name='index'),
    ]