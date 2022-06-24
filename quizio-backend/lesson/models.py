from django.db import models
from course.models import Course
from django.utils.text import slugify
# Create your models here.
class Lesson(models.Model):
    topic = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='lessons', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slug = models.SlugField()
    content = models.TextField()
    exert = models.TextField(default='')
    date_created = models.DateTimeField()

    def __str__(self):
        return f'{self.topic} - {self.course.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Lesson, self).save(*args , **kwargs)
