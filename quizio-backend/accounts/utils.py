from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .tokens import EmailActivationTokenGenerator
from threading import Thread
from django.core.mail import EmailMessage
from django.conf import settings

passwordResetTokenGenerator = PasswordResetTokenGenerator()
emailActivationTokenGenerator = EmailActivationTokenGenerator()

FRONTEND_URL = 'http://localhost:3000'

class EmailThread(Thread):
    def __init__(self , email):
        self.email = email
        Thread.__init__(self)

    def run(self):
        self.email.send()


def send_password_reset_mail(user):
    token = passwordResetTokenGenerator.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.id))
    email_subject ='Password Reset on Quizio'
    email_body= render_to_string('password_reset.html' , {
        'user':user,
        'token':token,
        'uidb64':uidb64,
        'domain':FRONTEND_URL
    })
    email = EmailMessage(from_email=settings.EMAIL_HOST_USER , subject=email_subject , body=email_body , to=[user.email])
    EmailThread(email).start()




def send_email_activation_mail(user):
    token = emailActivationTokenGenerator.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.id))
    email_subject = 'Email Activation on Quizio'
    email_body = render_to_string('email_activation.html', {
        'user':user,
        'token':token,
        'uidb4':uidb64,
        'domain':FRONTEND_URL
    })
    email = EmailMessage(from_email=settings.EMAIL_HOST_USER , subject=email_subject , body=email_body , to=[user.email])
    EmailThread(email).start()


def send_password_change_mail(user):
    pass