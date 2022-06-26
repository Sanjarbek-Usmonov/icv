from rest_framework import views, response, status, generics
from .models import Alloma, Century, Madrasa, Regions, SumMadrasa, MadrasaName
from django.http import Http404
from .serializers import CenturySerializer, MadrasaSerializer, AllomaSerializer, AllomaIDSerializer, RegionsSerializer, SumMadrasaSerializer, MadrasaNameSerializer
from django_filters.rest_framework import DjangoFilterBackend


class RegionsAPIView(views.APIView):
    def get(self, request):
        queryset = Regions.objects.all()
        serializer = RegionsSerializer(queryset, many=True)
        return response.Response(serializer.data)


class CenturyAPIView(views.APIView):
    def get(self, request):
        query = Century.objects.all()
        serializer = CenturySerializer(query, many=True)
        return response.Response(serializer.data)


class SumMadrasaView(generics.ListAPIView):
    serializer_class = SumMadrasaSerializer
    queryset = SumMadrasa.objects.all()
 

class MadrasaNameView(generics.ListAPIView):
    serializer_class = MadrasaNameSerializer
    queryset = MadrasaName.objects.all()


class MadrasaAPIView(views.APIView):
    def get(self, request):
        query = Madrasa.objects.all()
        serializer = MadrasaSerializer(query, many=True)
        return response.Response(serializer.data)

class AllomaAPIView(views.APIView):
    def get(self, request):
        query = Alloma.objects.all()
        serializer = AllomaSerializer(query, many=True, context={"request": request})
        return response.Response(serializer.data)


class AllomaIDAPIView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_object(pk)
        serializer = AllomaIDSerializer(queryset, context={"request": request})
        return response.Response(serializer.data)


    def get_object(self, pk):
        try:
            return Alloma.objects.get(pk=pk)
        except Alloma.DoesNotExist:
            raise Http404

