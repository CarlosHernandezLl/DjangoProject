# Create your views here.
# mi_aplicacion/views.py
from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'Pruebas/lista_libros.html', {'libros': libros})
