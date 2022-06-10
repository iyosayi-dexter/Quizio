from rest_framework.views import APIView
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .threads import MessageCreationThread,MessageSetSeenThread
from rest_framework.permissions import (
    IsAuthenticated , AllowAny
)

User = get_user_model()

class RetrieveMessagesView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            data = Message.objects.get_messages(user)
            serializer = MessageSerializer(data, many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class sendMessageView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user = request.user
        data = request.data
        receiver = data.get('receiver' , None)
        text = data.get('text', None)
        attachments = data.get('attachments' , None)

        # user cannot be an anonymous user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if receiver is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # receiver must be a valid user
        try:
            receiver_user = User.objects.get(id=receiver.get('id'), username=receiver.get('username'))
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # user must send either an attachments or a text
        if (attachments is None and text is None) or (attachments is None and len(text.strip()) < 1):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if receiver_user == user :
            # user sends a note to self
            message_inst = Message(sender=user , receiver=receiver_user , text=text , attachments=attachments , seen=True)
        else:
            # user sends a message to another user
            message_inst =Message(sender=user , receiver=receiver_user , text=text , attachments=attachments, seen=False)

        MessageCreationThread(message_inst).start()
        return Response(status=status.HTTP_200_OK)


class setSeenView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self , request):
        user = request.user
        data = request.data
        message_id = data.get('message_id', None)

        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if message_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user_messages = Message.objects.get_messages(user)
        try:
            message_inst = user_messages.get(id=message_id)
            MessageSetSeenThread(message_inst).start()
            return Response(status=status.HTTP_200_OK)
        except Message.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)