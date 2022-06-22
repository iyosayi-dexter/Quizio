from django.urls import path
from .views import RetrieveCoursesView


urlpatterns = [
    path('' , RetrieveCoursesView.as_view(), name='retrieve_course')
]