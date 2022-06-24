from django.urls import path
from .views import LessonDetailView, LessonRetrieveView

urlpatterns = [
    path('', LessonRetrieveView.as_view(), name='lesson_retrive'),
    path('<slug>/', LessonDetailView.as_view(), name='lesson_detail')
]