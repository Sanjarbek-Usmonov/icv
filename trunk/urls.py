from django.urls import path
from .views import SubjectAPIView, Subject_InfoAPIView, Subject_Extra_InfoAPIView,\
    FilterAPIView, BooksAPIView, WoScienceAPIView

urlpatterns = [
    path('subjects', SubjectAPIView.as_view()),
    path('<int:pk>/subject-info/', Subject_InfoAPIView.as_view()),
    path('subject-info/<int:pk>/subject-extra-info', Subject_Extra_InfoAPIView.as_view()),
    path('alloma-and-subjects', FilterAPIView.as_view()),
    path('books', BooksAPIView.as_view()),
    path('science', WoScienceAPIView.as_view()),
]
