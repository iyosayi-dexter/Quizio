from django.urls import path
from .views import RetrieveQuestionsView,SubmitQuizView , ChallangeView

urlpatterns = [
    path('questions/', RetrieveQuestionsView.as_view() , name='retrieve_questions'),
    path('submit/', SubmitQuizView.as_view(), name='submit_questions'),
    path('challange/' , ChallangeView.as_view(), name='challange')
]