from django.shortcuts import render

# Create your views here.
from .models import Singer, Song
from .serializer import SingerSerializer, SongSerializer
from rest_framework import viewsets

class Singerviewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class Songviewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    