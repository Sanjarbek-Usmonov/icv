from django.urls import path
from .views import CenturyAPIView, MadrasaAPIView, AllomaAPIView, AllomaIDAPIView, RegionsAPIView

urlpatterns = [
    path('centuries/', CenturyAPIView.as_view()),
    path('centuries/madrasas/', MadrasaAPIView.as_view()),
    path('centuries/madrasas/allomas', AllomaAPIView.as_view()),
    path('alloma/<int:pk>', AllomaIDAPIView.as_view()),
    path('regions/', RegionsAPIView.as_view()),
]