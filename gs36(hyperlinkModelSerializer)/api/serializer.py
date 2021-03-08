from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id','url', 'name', 'roll', 'city']

'''
#check any serializer on python manage.py shell
>>> from api.serializer import StudentSerializer
>>> serializer = StudentSerializer()
>>> print(repr(serializer))
StudentSerializer():
    id = IntegerField(label='ID', read_only=True)
    url = HyperlinkedIdentityField(view_name='student-detail')
    name = CharField(max_length=100)
    roll = IntegerField()
    city = CharField(max_length=100)
>>> 
'''