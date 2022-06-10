from django.contrib import admin

from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender' , 'receiver' , 'seen')

admin.site.register(Message, MessageAdmin)