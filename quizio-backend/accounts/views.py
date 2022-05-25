from .serializers import AuthTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework import status,permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .utils import send_password_reset_mail , send_email_activation_mail , send_password_change_mail, emailActivationTokenGenerator , passwordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str


User = get_user_model()


class AuthTokenPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self , request):
        data = request.data
        email=data.get('email' , None)
        username = data.get('username' , None)
        password = data.get('password' , None)
        re_password = data.get('re_password' , None)

        if email is None or username is None or password is None or re_password is None:
            return Response({'detail':'invalid credentials'} ,status= status.HTTP_400_BAD_REQUEST)

        if password != re_password:
            return Response({'detail':'Passwords do not match'} , status= status.HTTP_400_BAD_REQUEST)

        if len(username.strip()) < 3:
            return Response({'detail': 'Username must be at least 3 characters long'} , status= status.HTTP_400_BAD_REQUEST)

        normalized_email = email.strip().lower()

        try:
            User.objects.get(email=normalized_email)
            return Response({'detail':'User with this email already exists'} , status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:

            User.objects.create_user(normalized_email, username , password)
            return Response({'detail':'Account Creation successfull'} , status=status.HTTP_201_CREATED)


class PasswordResetView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        email = data.get('email' , None)

        if email is None:
            return Response({'detail':'Invalid credentails'} , status= status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            send_password_reset_mail(user)
            return Response(status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'detail':'User does not exist'} , status= status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request , uidb64 , token):
        data = request.data
        password = data.get('password' , None)
        uid = force_str(urlsafe_base64_decode(uidb64))
        if password is None:
            return Response({'detail':'Invalid credentials passed'} , status=status.HTTP_200_OK)


        try:
            user = User.objects.get(id=uid)
            if passwordResetTokenGenerator.check_token(user, token):
                user.set_password(password)
                user.save()
                send_password_change_mail(user)
                return Response({'detail':'Password reset successful'}, status=status.HTTP_200_OK)
            else:
                raise ValueError('Inavlid token')
        except:
            return Response({'detail':'Password reset failed'} , status=status.HTTP_400_BAD_REQUEST)




class EmailVerficationView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request , uidb64 , token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        try:
            user = User.objects.get(id = uid)

            if user.is_email_verified and emailActivationTokenGenerator.check_token(user , token):
                return Response({'detail':'Email Already verified'}, status=status.HTTP_200_OK)


            if emailActivationTokenGenerator.check_token(user , token):
                user.email_verified=True
                user.save()
                return Response({'detail':'Email Activation successful'} , status=status.HTTP_200_OK)
            else:
                raise ValueError('Invalid token')

        except:
            return Response({'detail':'Invalid credentials'} , status= status.HTTP_400_BAD_REQUEST)


class RequestEmailVerficationView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self , request):
        data = request.data
        email = data.get('email' , None)

        if email is None:
            return Response({'detail':'Invalid credentials'} , status=status.HTTP_400_BAD_REQUEST)

        try:

            user = User.objects.get(email=email)
            if user.is_email_verified:
                return Response({'detail':'Email already verified'} , status=status.HTTP_200_OK)
            else:
                send_email_activation_mail(user)
                return Response({'detail':'Instructions to verify your mail have been sent to your mail'} , status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'detail':'User does not exist'}, status= status.HTTP_400_BAD_REQUEST)



