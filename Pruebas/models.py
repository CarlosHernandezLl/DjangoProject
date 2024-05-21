# Create your models here.
# mi_aplicacion/models.py
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    publicado_el = models.DateField()

    def __str__(self):
        return self.titulo
