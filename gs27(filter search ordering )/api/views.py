from django.shortcuts import render

# Create your views here.
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

class StudentList(ListAPIView):
    #filtering
    queryset = Student.objects.all()
    #queryset = Student.objects.all(passby ='piyush')
    serializer_class = StudentSerializer
    #filters querysets passed by that user
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)

