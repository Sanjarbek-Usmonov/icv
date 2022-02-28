from rest_framework import views, response, filters, generics
from .serializers import SubjectSerializer, Subject_InfoSerializer, Subject_Extra_InfoSerializer, BooksSerializer, WoScienceSerializer
from .models import Subject, Subject_Info, Subject_Extra_Info, Books, WoScience
from base.models import Alloma
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend

class SubjectAPIView(views.APIView):
    def get(self, request, pk):
        queryset = self.get_object(pk)
        query = Subject.objects.filter(menu_id=queryset.pk)
        serializer = SubjectSerializer(query, many=True, context={'request': request})
        return response.Response(serializer.data)

    def get_object(self, pk):
        try:
            return Alloma.objects.get(pk=pk)
        except Alloma.DoesNotExist:
            raise Http404

class Subject_InfoAPIView(views.APIView):
    def get(self, request, pk):
        queryset = self.get_object(pk)
        query = Subject_Info.objects.filter(subject_id=queryset.pk)
        serializer = Subject_InfoSerializer(query, many=True, context={'request': request})
        return response.Response(serializer.data)

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

class Subject_Extra_InfoAPIView(views.APIView):
    def get(self, request, pk):
        queryset = self.get_object(pk)
        query = Subject_Extra_Info.objects.filter(subject_id=queryset.pk)
        serializer = Subject_Extra_InfoSerializer(query, many=True, context={'request': request})
        return response.Response(serializer.data)

    def get_object(self, pk):
        try:
            return Subject_Info.objects.get(pk=pk)
        except Subject_Info.DoesNotExist:
            raise Http404

class FilterAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'menu__name']

class BooksAPIView(views.APIView):
    def get(self, request):
        queryset = Books.objects.all()
        serializer = BooksSerializer(queryset, many=True)
        return response.Response(serializer.data)

class WoScienceAPIView(views.APIView):
    def get(self, request):
        queryset = WoScience.objects.all()
        serializer = WoScienceSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)
