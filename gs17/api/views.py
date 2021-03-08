from .models import *
from . serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions

# WholeCRUD operations in this two lines using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [DjangoModelPermissions] # gives specific permission to the user who can POST, who can Delete

