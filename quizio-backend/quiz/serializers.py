from rest_framework.serializers import ModelSerializer
from .models import Question


class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id' , 'question' ,'option_a', 'option_b' , 'option_c' , 'option_d')

