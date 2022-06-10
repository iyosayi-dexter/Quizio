from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Profile
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Customizing token claims
        token['username'] = user.username
        token['email'] = user.email
        token['email_verified'] = user.email_verified

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username' , 'id' , )

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('user','about','xp','profile_image')