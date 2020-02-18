from django.shortcuts import render

# Create your views here.

def bosque_list(request):
    return render(request, 'bosque/bosque_list.html', {})