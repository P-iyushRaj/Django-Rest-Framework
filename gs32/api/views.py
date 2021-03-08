from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView

from .mypagination import MyPageNumberPagination

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination
    #http://127.0.0.1:8000/studentapi/?page=1
    #http://127.0.0.1:8000/studentapi/?p=1
    #http://127.0.0.1:8000/studentapi/?page=1&records=6
    

