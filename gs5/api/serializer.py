from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class meta:
        modle = Student
        fields = ['name', 'roll', 'city']

        #fields = '__all__'
        #exclude = ['name']


