from rest_framework import views, response, status
from .models import Alloma, Century, Madrasa
from django.http import Http404
from .serializers import CenturySerializer, MadrasaSerializer, AllomaSerializer, AllomaIDSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CenturyAPIView(views.APIView):
    def get(self, request):
        query = Century.objects.all()
        serializer = CenturySerializer(query, many=True)
        return response.Response(serializer.data)

class MadrasaAPIView(views.APIView):
    def get(self, request):
        query = Madrasa.objects.all()
        serializer = MadrasaSerializer(query, many=True)
        return response.Response(serializer.data)

class AllomaAPIView(views.APIView):
    def get(self, request):
        query = Alloma.objects.all()
        serializer = AllomaSerializer(query, many=True)
        return response.Response(serializer.data)


class AllomaIDAPIView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_object(pk)
        serializer = AllomaIDSerializer(queryset)
        return response.Response(serializer.data)


    def get_object(self, pk):
        try:
            return Alloma.objects.get(pk=pk)
        except Alloma.DoesNotExist:
            raise Http404



# class FooFilter(DjangoFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         filter_class = self.get_filter_class(view, queryset)
#         if filter_class:
#             return filter_class(request.query_params, queryset=queryset, request=request).qs
#         return queryset
#
# class Foo(views.APIView):
#     filter_fields = ('name')
#     def get(self, request, format=None):
#         queryset = Madrasa.objects.all()
#         ff = FooFilter()
#         filtered_queryset = ff.filter_queryset(request, queryset, self)
#         if filtered_queryset.exists():
#             serializer = MadrasaSerializer(queryset, many=True)
#             return response.Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return response.Response([], status=status.HTTP_200_OK)
