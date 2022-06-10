from rest_framework.serializers import ModelSerializer , DateTimeField
from .models import Message
from accounts.serializers import UserSerializer

class MessageSerializer(ModelSerializer):
    date_sent = DateTimeField(format='%b %d %Y, %I:%H%p')
    sender = UserSerializer()
    receiver = UserSerializer()
    class Meta:
        model= Message
        fields = '__all__'