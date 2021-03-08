from .models import *
from . serializers import *
from rest_framework import viewsets

# WholeCRUD operations in this two lines using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# read only ( list and retrieve) operations in this two lines using ModelViewSet
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
