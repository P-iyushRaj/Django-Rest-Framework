#using custom permissions
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# WholeCRUD operations in this two lines using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [MyPermission]

    #python manage.py drf_create_token user1
    
