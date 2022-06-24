from rest_framework.serializers import ModelSerializer
from .models import Lesson


class LessonListSeriaizer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('topic', 'thumbnail', 'exert', 'date_created',)

class LessonDetailSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('topic', 'thumbnail', 'date_created', 'content',  )