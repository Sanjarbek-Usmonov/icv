from rest_framework import serializers
from .models import Subject, Subject_Info, Subject_Extra_Info, Books, WoScience

class SubjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'image_url', 'menu')

class Subject_InfoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = Subject_Info
        fields = ('id', 'text', 'image_url', 'subject')

class Subject_Extra_InfoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = Subject_Extra_Info
        fields = ('id', 'text', 'image_url', 'subject')

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class WoScienceSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = WoScience
        fields = ('id', 'info', 'image_url', 'author_id')
