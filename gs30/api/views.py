from django.shortcuts import render

# Create your views here.
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

#order filter
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
    #filtering
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'id']


