#using custom permissions
from .models import *
from .serializers import *
from rest_framework import viewsets
#rom rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#custom authentication
from api.customauth import CustomAuthentication

# WholeCRUD operations in this two lines using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #uthentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    
