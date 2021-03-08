from django.shortcuts import render

# Create your views here.
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    #filtering
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','city']
    #search_fields = ['^name']   #startwith
    #search_fields = ['=name']   #exactm match
    #search_fields = ['@name']   #full text search
    #search_fields = ['$name']   #Regex search
