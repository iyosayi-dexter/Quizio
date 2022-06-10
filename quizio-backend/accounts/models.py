from django.contrib.auth.models import (AbstractUser)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_email_activation_mail
from django.contrib.auth import get_user_model
from .managers import AcccountManager


class Account(AbstractUser):
    # properties
    email = models.EmailField(max_length=255 , unique=True, verbose_name='email address')
    username = models.CharField(max_length=40)

    # Permissions
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)

    # model manager
    objects = AcccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_email_verified(self):
        return self.email_verified

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(Account , on_delete=models.CASCADE, related_name='user')
    profile_image = models.ImageField(upload_to='users_profiles', null=True, blank=True)
    about= models.TextField(null=True, blank=True)
    xp = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save , sender=Account)
def user_creation_receiver(sender , instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        try:
            send_email_activation_mail(instance)
        except:
            pass

