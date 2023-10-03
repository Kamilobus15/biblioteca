from rest_framework import viewsets
from .serializer import *
from .models import *


# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
