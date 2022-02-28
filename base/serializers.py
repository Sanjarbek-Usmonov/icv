from rest_framework import serializers
from .models import Century, Madrasa, Alloma, AllomaMenu


class CenturySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    century = serializers.CharField(max_length=100, read_only=True)
    sum_madrasa = serializers.CharField(max_length=100, read_only=True)

class MadrasaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
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

class RegionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, read_only=True)
