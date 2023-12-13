from rest_framework import viewsets
from .serializer import ProfesorSerializer,AlumnoSerializer
from .models import Profesor, Alumno

# Create your views here.

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer




