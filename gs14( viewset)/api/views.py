from rest_framework.response import Response 
from .models import *
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
#videl 17
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print('basename', self.basename)
        print('basename', self.basename)
        print('basename', self.basename)
        print('basename', self.basename)
        print('basename', self.basename)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    def retrieve(self,request, pk=None):
        id =pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    def create(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request, pk=None):
        id =pk
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    def partial_update(self,request, pk=None):
        id =pk
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({'msg':'data deleted'})

