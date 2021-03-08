from rest_framework import serializers

from .models import Singer, Song

class SingerSerializer(serializers.ModelSerializer):
    #IF WE WANRT THE SONG SUNG BY THET SINGER
    #song = serializers.StringRelatedField(many=True, read_only=True)   #song name
    #song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)   #song id
    #song = serializers.HyperlinkedRelatedField(many=True, read_only=True,  #song link
    #view_name = 'song-detail') 
    #song = serializers.SlugRelatedField(many=True, read_only=True,         #song name
    #slug_field = 'title')
    song = serializers.HyperlinkedIdentityField( view_name = 'song-detail')   #song link
    
    
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration' ]