from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView

from .mypagination import MyCursorPagination

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination
    #http://127.0.0.1:8000/studentapi/?page=1
    #http://127.0.0.1:8000/studentapi/?p=1
    #http://127.0.0.1:8000/studentapi/?page=1&records=6
    
    #http://127.0.0.1:8000/studentapi/?limit=4&offset=8
    #start from 9th item and will show 4 in each page

