from rest_framework import serializers
from .models import Subject, Subject_Info, Subject_Extra_Info, Books, WoScience

class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)
    menu = serializers.CharField(read_only=True)

class Subject_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Info
        fields = '__all__'

class Subject_Extra_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Extra_Info
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class WoScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WoScience
        fields = '__all__'
