from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class MessageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_messages(self,user):
        lookup = Q(sender=user) | Q(receiver=user)
        return self.get_queryset().filter(lookup)


class Message(models.Model):
    sender= models.ForeignKey(User, on_delete=models.CASCADE , related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE , related_name='receiver')
    text = models.TextField(null=True, blank=True)
    attachments= models.JSONField(null=True, blank=True)
    seen = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)
    objects = MessageManager()
