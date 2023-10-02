from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)