from django.urls import path
from . import views

urlpatterns = [
	path('', views.bosque_list, name='bosque_list'),
	]