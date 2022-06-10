from django.urls import path
from .views import sendMessageView, RetrieveMessagesView, setSeenView

urlpatterns = [
    path('send-message/' , sendMessageView.as_view(), name='send_message'),
    path('retrieve-messages/' , RetrieveMessagesView.as_view(), name='retrieve_message'),
    path('set-seen/' , setSeenView.as_view(), name='set_seen'),
]