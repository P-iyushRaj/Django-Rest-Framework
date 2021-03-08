from rest_framework import serializers

class StidentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

