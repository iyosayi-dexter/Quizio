from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title' , 'date_created' ,)


admin.site.register(Course, CourseAdmin)