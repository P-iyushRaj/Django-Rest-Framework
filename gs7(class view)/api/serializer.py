from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
        #validaators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('name should staartswith r')
        return value
    name = serializers.CharField(max_length = 100, read_only=True, validators = [start_with_r])        
    #name = serializers.CharField(max_length = 100, read_only=True)
    class meta:
        modle = Student
        fields = ['name', 'roll', 'city']
        #read_only_fields = ['name', 'city']
        #extra_kwargs = {'name' : {'read_only':True}}



    #field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seaat full')
        return value

    #Object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() =='rohit' and ct.lower()!='ranchi':
            raise serializers.ValidationError('city must be ranchi')
        return data
'''
#validaators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name should staartswith r')
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length =100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length =100)
    '''