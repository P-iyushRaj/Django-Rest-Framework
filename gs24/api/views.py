#using custom permissions
from .models import *
from .serializers import *
from rest_framework import viewsets
#rom rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# WholeCRUD operations in this two lines using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #uthentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    #http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer token_here'
    permission_classes = [IsAuthenticated]

#after login going to get token then using that token our api can be got
#to post the data using token
#http -f POST http://127.0.0.1:8000/studentapi/ name=raj roll=100 city=bokaro 'Authentication:Bearer token_here'
#http PUT http://127.0.0.1:8000/studentapi/2/ name=raj roll=100 city=bokaro 'Authentication:Bearer token_here'
#http DELETE http://127.0.0.1:8000/studentapi/2/ name=raj roll=100 city=bokaro 'Authentication:Bearer token_here'
