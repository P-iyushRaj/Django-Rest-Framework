#using proper DRF(django rest framework)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
'''
@api_view() #or @api_view('GET')
def hello_world(request):
    return Response({'msg':'hello world'})

@api_view(['POST'])
def hello_world(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'this is post request'})
'''
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        print(request.data)
        return Response({'msg':'this is GET request', 'data': request.data})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'this is post request', 'data': request.data})



    
