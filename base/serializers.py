from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Century, Madrasa, Alloma, AllomaMenu, SumMadrasa, MadrasaName

class RegionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, read_only=True)


class CenturySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    century = serializers.CharField(max_length=100, read_only=True)


class SumMadrasaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'region_id', 'century_id', 'sum_madrasa']
        model = SumMadrasa


class MadrasaNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = MadrasaName


class MadrasaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    madrasa_id = serializers.PrimaryKeyRelatedField(read_only=True)
    century_id = serializers.PrimaryKeyRelatedField(read_only=True)
    region_id = serializers.PrimaryKeyRelatedField(read_only=True)


class AllomaSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = Alloma
        fields = ('id', 'name', 'madrasa_alloma', 'image_url')

class AllomaIDSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)

    class Meta:
        model = Alloma
        fields = ('id', 'name', 'birth_year', 'birth_area', 'image_url', 'madrasa_alloma', 'about')


