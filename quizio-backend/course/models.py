from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='courses', null=True , blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title