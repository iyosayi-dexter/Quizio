from rest_framework.test import APITestCase , APIClient
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from django.urls import reverse
from django.contrib.auth import get_user_model
from chat.models import Message
from chat.views import RetrieveMessagesView, sendMessageView,setSeenView

User = get_user_model()

class TestChatView(APITestCase):
    def setUp(self):
        self.test_user1 = User.objects.create_user(username='test_0' , password='ReallyStrongPassword123' , email='te0@test.test')
        self.test_user2 = User.objects.create_user(username='test_1' , password='ReallyStrongPassword123' , email='te1test.test')
        self.send_message_url = reverse('send_message')
        self.retrieve_message_url = reverse('retrieve_message')
        self.set_message_seen_url = reverse('set_seen')
        self.api_client = APIClient()

        Message.objects.create(sender=self.test_user1, receiver=self.test_user2, text='testing, does it work?')
        Message.objects.create(sender=self.test_user2, receiver=self.test_user1, text='lets gooooooo')



    def test_send_message_isunauthorized(self):
        data = {}
        res = self.client.post(self.send_message_url, data , format='json')
        self.assertEqual(res.status_code , HTTP_401_UNAUTHORIZED)

    def test_set_see_isunauthorized(self):
        data = {}
        res = self.client.post(self.set_message_seen_url, data , format='json')
        self.assertEqual(res.status_code , HTTP_401_UNAUTHORIZED)

    def test_retrieve_message_isunauthorized(self):
        data = {}
        res = self.client.post(self.retrieve_message_url, data , format='json')
        self.assertEqual(res.status_code , HTTP_401_UNAUTHORIZED)

    def test_retrieve_message_authorized(self):
        res = self.api_client.get(self.retrieve_message_url)





