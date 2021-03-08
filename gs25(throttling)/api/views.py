#using custom permissions
from .models import *
from .serializers import *
from rest_framework import viewsets
#rom rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

from api.throtlling import JackRateThrottle

# WholeCRUD operations in this two lines using ModelViewSet
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    #throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AnonRateThrottle, JackRateThrottle]
    #for authenticated user it sets api/hour to 3
