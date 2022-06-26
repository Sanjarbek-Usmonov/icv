from numpy import require
from rest_framework import serializers
from .models import Subject
from base.models import Books, WoScience, Subject_Info, Subject_Extra_Info

class SubjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'image')

class Subject_InfoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = Subject_Info
        fields = ('id', 'text', 'image_url', 'alloma_id', 'subject_id')

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
