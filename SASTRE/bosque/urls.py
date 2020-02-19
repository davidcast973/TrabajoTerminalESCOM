from django.urls import path
from . import views

urlpatterns = [
	path('', views.animal_list, name='animal_list'),
	path('bosque/animal/', views.animal_list, name='animal_list'),
	path('bosque/planta/', views.planta_list, name='planta_list'),
	path('bosque/animal/<int:pk>/', views.animal_detalle, name='animal_detalle')
	]