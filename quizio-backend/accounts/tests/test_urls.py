from django.test import SimpleTestCase


from django.test import SimpleTestCase
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import reverse, resolve
from accounts.views import (
    EmailVerficationView, RequestEmailVerficationView , SignUpView , PasswordResetView , PasswordResetConfirmView ,AuthTokenPairView
)

class TestUrls(SimpleTestCase):
    def test_token_pair_url_resolved(self):
        url = reverse('token_obtain_pair')
        self.assertEqual(resolve(url).func.view_class, AuthTokenPairView)

    def test_token_refresh_url_resolved(self):
        url = reverse('token_refresh')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_signup_resolved(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func.view_class, SignUpView)

    def test_email_verify_resolved(self):
        url = reverse('email_verify' , args=['uid' , 'token'])
        self.assertEqual(resolve(url).func.view_class, EmailVerficationView)

    def test_email_request_verify_resolved(self):
        url = reverse('email_verify_request')
        self.assertEqual(resolve(url).func.view_class, RequestEmailVerficationView)

    def test_password_reset_resolved(self):
        url = reverse('password_reset')
        self.assertEqual(resolve(url).func.view_class, PasswordResetView)

    def test_password_reset_confirm(self):
        url = reverse('password_reset_confirm' , args=['uid' , 'token'])
        self.assertEqual(resolve(url).func.view_class, PasswordResetConfirmView)

