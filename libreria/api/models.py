from django.db import models


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.ForeignKey('autor', on_delete=models.CASCADE, null=True)
    editorial = models.ForeignKey('editorial', on_delete=models.CASCADE, null=True)
    genero = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)


class Editorial(models.Model):
    nombre = models.CharField(max_length=30)
    fundacion = models.IntegerField()
    fundador = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
