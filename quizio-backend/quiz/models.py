from django.db import models
from course.models import Course
from .managers import QuestionsManager
from django.contrib.auth import get_user_model
from datetime import timedelta, datetime
User = get_user_model()


OPTION_CHOICES = [
    ('A', 'option_a'),
    ('B', 'option_b'),
    ('C', 'option_c'),
    ('D', 'option_d'),
]

MODE_CHOICES = [
    ('BASIC', 'BASIC'),
    ('MEDIUM', 'MEDIUM'),
    ('HARD', 'HARD'),
]


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mode = models.CharField(max_length=40, choices=MODE_CHOICES, default=MODE_CHOICES[0])
    question = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1, choices=OPTION_CHOICES, default=OPTION_CHOICES[0])
    date_created = models.DateTimeField(auto_now=True)
    objects = QuestionsManager()

    def __str__(self):
        return self.question


class Challange(models.Model):
    challangee = models.ForeignKey(User, on_delete=models.CASCADE , related_name='challangee')
    challanger = models.ForeignKey(User, on_delete=models.CASCADE , related_name='challanger')
    challangee_score = models.IntegerField(default=0)
    challanger_score = models.IntegerField(default=0)
    quiz = models.JSONField()
    accepted= models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField()


    def save(self, *args , **kwargs):
        self.expiry =  timedelta(days=1) + datetime.now()
        super(Challange, self).save(*args , **kwargs)

    def __str__(self):
        return f'{self.challangee.username} vs {self.challanger.username} expires {self.expiry}'