from django.contrib.auth.models import ( BaseUserManager , AbstractUser)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_email_activation_mail


class AcccountManager(BaseUserManager):
    def create_user(self, email , username , password=None):
        if not email:
            raise ValueError('Email is required')

        if not username:
            raise ValueError('Username is required')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email , username , password=None):
        user = self.create_user(email , username , password)
        user.superuser=True
        user.admin=True
        user.staff=True
        user.save(using=self.db)
        return user


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


@receiver(post_save , sender=Account)
def user_creation_receiver(sender , instance, created, **kwargs):
    if created:
        send_email_activation_mail(instance)
