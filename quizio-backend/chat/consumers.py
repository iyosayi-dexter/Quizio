import json
from pydoc import text
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Message
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from urllib.parse import parse_qs
from .utils import decode_token  , get_chat_name , load_message
from .threads import CreateMessageThread

User = get_user_model()


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        query_string = parse_qs(force_str(self.scope['query_string']))
        token, = query_string['token']
        decoded_token = decode_token(token)

        if decoded_token is None:
            self.user = None
            self.close()
            return

        self.user = User.objects.get(username=decoded_token['username'] , id=decoded_token['user_id'] , email=decoded_token['email'])
        self.chat_name = get_chat_name(self.user)


        async_to_sync(self.channel_layer.group_add)(
            self.chat_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        if self.user == None:
            return
        async_to_sync(self.channel_layer.group_discard)(
            self.chat_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)


        try:
            receiver_user = User.objects.get(username=text_data_json['receiver']['username'], id=text_data_json['receiver']['id'])
        except User.DoesNotExist:
            return

        receiver_chat_name = get_chat_name(receiver_user)

        message_inst = Message(sender=self.user, receiver=receiver_user, text=text_data_json['text'], attachments=text_data_json['attachments'])
        mesage_thread = CreateMessageThread(message_inst)
        mesage_thread.start()
        message_id = mesage_thread.join()


        message_data = load_message(self.user, message_id , text_data_json)

        # send to receiver
        async_to_sync(self.channel_layer.group_send)(
            receiver_chat_name,
            {
                'type':'chat_message',
                'message_data':json.dumps(message_data)
            }
        )

        # echo back to user
        async_to_sync(self.channel_layer.group_send)(
            self.chat_name,
            {
                'type':'chat_message',
                'message_data':json.dumps(message_data)
            }
        )

    def chat_message(self, event):
        message = event['message_data']
        self.send(text_data=message)

