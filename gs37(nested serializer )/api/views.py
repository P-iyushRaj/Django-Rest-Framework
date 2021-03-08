from django.shortcuts import render

# Create your views here.
from .serializer import SingerSerializer, SongSerializer
from .models import Singer, Song
from rest_framework import viewsets

class SingerViewSet(viewsets.ModelViewSet):
    queryset= Singer.objects.all()
    serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
