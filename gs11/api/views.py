from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

class Student_api(APIView):
    def get(self, request, pk = None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many =True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #COMPLETE UPDATE
    def put(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #partial update
    def patch(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu,data=request.data,
        partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk=None,format=None):
        id = pk
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({'msg':'data deleted'})
        
