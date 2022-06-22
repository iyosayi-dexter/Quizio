from rest_framework.serializers import ModelSerializer
from .models import Course


class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('title' , 'id' , 'thumbnail',)