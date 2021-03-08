from .models import *
from .serializers import StudentSerializer
from rest_framework.generics import DestroyAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
'''
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#need pk
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

