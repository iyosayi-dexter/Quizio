from django.contrib import admin
from .models import Lesson
from django_summernote.admin import SummernoteModelAdmin



class LessonAdmin(SummernoteModelAdmin):
    list_display = ('topic', 'course', 'date_created',)
    exclude = ('date_created',)
    summernote_fieds = ('content',)


admin.site.register(Lesson , LessonAdmin)