from rest_framework import routers
from django.urls import path,include
from .views import ProfesorViewSet,AlumnoViewSet

ruta = routers.DefaultRouter()
ruta.register('profesor',ProfesorViewSet)
ruta.register('alumno' ,AlumnoViewSet)

urlpatterns = [
    path('', include(ruta.urls)),
]
