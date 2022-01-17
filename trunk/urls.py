from django.urls import path
from .views import SubjectAPIView, Subject_InfoAPIView, Subject_Extra_InfoAPIView, FilterAPIView

urlpatterns = [
    path('alloma/<int:pk>/subject/', SubjectAPIView.as_view()),
    path('alloma/subject/<int:pk>/subject-info/', Subject_InfoAPIView.as_view()),
    path('alloma/subject/subject-info/<int:pk>/subject-extra-info', Subject_Extra_InfoAPIView.as_view()),
    path('alloma-and-subjects', FilterAPIView.as_view()),
]
