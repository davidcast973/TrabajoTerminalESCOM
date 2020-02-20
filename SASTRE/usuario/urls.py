from django.urls import path
from . import views

urlpatterns = [
	path('<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('nuevo/', views.usuario_new, name='usuario_new'),
    path('<int:pk>/edicion/', views.usuario_edit, name='usuario_edit'),
]