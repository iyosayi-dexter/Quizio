from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from accounts.utils import passwordResetTokenGenerator , emailActivationTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

User = get_user_model()

class TestView(APITestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username='test_0' , password='ReallyStrongPassword123' , email='te0@test.test')

    # testing for user creation
    def test_create_user(self):
        url = reverse('signup')
        data = {'username':'test' , 'email':'te@test.test' , 'password':'ReallyStrongPassword123' , 're_password':'ReallyStrongPassword123'}
        res = self.client.post(url , data , format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count() , 2)

        data = {}
        res = self.client.post(url , data , format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        data = {'username':self.test_user.username , 'email':self.test_user.email, 'password':'ReallyStrongPassword123' , 're_password':'ReallyStrongPassword123'}
        res = self.client.post(url , data , format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # testing for auth tokens(jwt)
    def test_auth_tokens(self):
        url = reverse('token_obtain_pair')
        data = {'email':'te0@test.test' , 'password':'ReallyStrongPassword123'}
        res = self.client.post(url , data , format='json')
        self.assertEqual(res.status_code , status.HTTP_200_OK)

        # Ensuring access and refresh tokens were returned
        self.assertTrue(res.data.get('refresh', None) != None)
        self.assertTrue(res.data.get('access', None) != None)

        # Testing refresh access token
        url = reverse('token_refresh')
        data = {'refresh': res.data.get('refresh')}
        res = self.client.post(url , data , format='json')

        # Ensuring access and refresh tokens were returned on refresh
        self.assertTrue(res.data.get('refresh', None) != None)
        self.assertTrue(res.data.get('access', None) != None)

        #Ensuring no token is returned for a user that does not exist
        url = reverse('token_obtain_pair')
        data = {'email':'does@not.exist' , 'password':'IDontExist123'}
        res = self.client.post(url , data , format='json')

        self.assertTrue(res.data.get('refresh', None) == None)
        self.assertTrue(res.data.get('access', None) == None)

    # testing for request email verification
    def test_request_email_verfy(self):
        url = reverse('email_verify_request')
        data = {'email': self.test_user.email}
        res = self.client.post(url, data , format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        data = {}
        res = self.client.post(url , data, format='json')
        self.assertEqual(res.status_code , status.HTTP_400_BAD_REQUEST)

        data = {'email':'does@not.exist'}
        res = self.client.post(url , data, format='json')
        self.assertEqual(res.status_code , status.HTTP_400_BAD_REQUEST)

    # testing for email verification
    def test_email_verify(self):
        token = emailActivationTokenGenerator.make_token(self.test_user)
        uidb64 = urlsafe_base64_encode(force_bytes(self.test_user.id))
        url = reverse('email_verify' , args=[uidb64 , token])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        fake_token = 'somefalselygenerateedToken'
        url = reverse('email_verify' , args=[uidb64 , fake_token])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        fake_uid = urlsafe_base64_encode(force_bytes(400))
        url = reverse('email_verify' , args=[fake_uid , token])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    # testing for password reset
    def test_password_reset(self):
        url = reverse('password_reset')
        data = {'email':self.test_user.email}
        res = self.client.post(url , data , format='json')
        self.assertEqual(res.status_code , status.HTTP_200_OK)

        data = {}
        res = self.client.post(url , data , format='json')
        self.assertEqual(res.status_code , status.HTTP_400_BAD_REQUEST)

        data = {'email':'does@not.exist'}
        res = self.client.post(url , data, format='json')
        self.assertEqual(res.status_code , status.HTTP_400_BAD_REQUEST)


    def test_password_reset_confirm(self):
        token = passwordResetTokenGenerator.make_token(self.test_user)
        uidb64 = urlsafe_base64_encode(force_bytes(self.test_user.id))
        url = reverse('password_reset_confirm' , args=[uidb64 , token])
        data = {'password':'NewReallyStrongPassword123'}
        res = self.client.post(url, data , format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        fake_token = 'somefalselygenerateedToken'
        url = reverse(f'password_reset_confirm' , args=[uidb64 , fake_token])
        data = {'password':'NewReallyStrongPassword123'}
        res = self.client.post(url, data , format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


        fake_uid = urlsafe_base64_encode(force_bytes(self.test_user.id))
        url = reverse(f'password_reset_confirm' , args=[fake_uid , token])
        data = {'password':'NewReallyStrongPassword123'}
        res = self.client.post(url, data , format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)






