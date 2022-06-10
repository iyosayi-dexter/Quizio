from django.test import SimpleTestCase
from django.urls import reverse, resolve
from chat.views import RetrieveMessagesView , sendMessageView ,setSeenView


class TestUrls(SimpleTestCase):
    def test_token_pair_url_resolved(self):
        url = reverse('send_message')
        self.assertEqual(resolve(url).func.view_class, sendMessageView)

    def test_token_pair_url_resolved(self):
        url = reverse('set_seen')
        self.assertEqual(resolve(url).func.view_class, setSeenView)


    def test_token_pair_url_resolved(self):
        url = reverse('retrieve_message')
        self.assertEqual(resolve(url).func.view_class, RetrieveMessagesView)
