from django.urls import path
from . import views

urlpatterns = [
	path('', views.animal_list, name='animal_list'),
	path('bosque/animal/', views.animal_list, name='animal_list'),
	path('bosque/planta/', views.planta_list, name='planta_list'),
	path('bosque/animal/<int:pk>/', views.animal_detalle, name='animal_detalle'),
	path('bosque/faunas/', views.faunas_list, name='faunas_list'),
	path('bosque/faunas/<int:pk>', views.fauna_detalle, name='fauna_detalle'),
	]