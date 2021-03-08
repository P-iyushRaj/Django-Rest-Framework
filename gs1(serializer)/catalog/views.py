from django.shortcuts import render
from .models import Student
from .serializer import StidentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# model instance for one data
def stuinfo(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StidentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = 'application/json')

# queryset get all data
def stuinfoquery(request):
    stu = Student.objects.all()
    serializer = StidentSerializer(stu, many = True)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type = 'application/json')

    #can also use JsonResponse
    return JsonResponse(serializer.data, safe = False)