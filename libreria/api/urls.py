from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'libros', views.LibroViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'editorial', views.EditorialViewSet)

urlpatterns = [
    path('', include(router.urls))
]
