from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(max_length = 100, read_only=True)
    class meta:
        modle = Student
        fields = ['name', 'roll', 'city']
        #read_only_fields = ['name', 'city']
        #extra_kwargs = {'name' : {'read_only':True}}
