from rest_framework_simplejwt.views import TokenRefreshView
from .views import AuthTokenPairView, EmailVerficationView, RequestEmailVerficationView , SignUpView , PasswordResetView , PasswordResetConfirmView, getUsersView
from django.urls import path

urlpatterns = [
    path('token/', AuthTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/' ,SignUpView.as_view() , name='signup'),
    path('email-verify/<str:uidb64>/<str:token>/' , EmailVerficationView.as_view() , name='email_verify'),
    path('email-request-verify/' , RequestEmailVerficationView.as_view() , name='email_verify_request'),
    path('password-reset/' , PasswordResetView.as_view() , name='password_reset'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    path('users' , getUsersView.as_view(), name='get_users')
]