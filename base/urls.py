from django.urls import path
from .views import CenturyAPIView, MadrasaAPIView, AllomaAPIView, AllomaIDAPIView, RegionsAPIView, SumMadrasaView, MadrasaNameView

urlpatterns = [
    path('regions/', RegionsAPIView.as_view()),
    path('centuries/', CenturyAPIView.as_view()),
    path('sum-madrasa/', SumMadrasaView.as_view()),
    path('madrasas/', MadrasaAPIView.as_view()),
    path('madrasa/list', MadrasaNameView.as_view()),
    path('centuries/madrasas/allomas', AllomaAPIView.as_view()),
    path('alloma/<int:pk>', AllomaIDAPIView.as_view()),
]