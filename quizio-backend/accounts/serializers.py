from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Customizing token claims
        token['username'] = user.username
        token['email'] = user.email
        token['email_verified'] = user.email_verified

        return token