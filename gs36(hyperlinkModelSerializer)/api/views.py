from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
