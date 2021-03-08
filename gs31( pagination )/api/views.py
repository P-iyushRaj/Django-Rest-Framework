from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


