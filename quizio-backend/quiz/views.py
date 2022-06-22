from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST , HTTP_200_OK
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionsSerializer
from django.contrib.auth import get_user_model
from .models import Challange
import random
from .models import Question
from course.models import Course

User = get_user_model()

class RetrieveQuestionsView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        data = request.data

        course = data.get('course' , None)
        nques = data.get('nques' , None)
        mode = data.get('mode' , None)

        if course is None or nques is None or mode is None :
            return Response(status=HTTP_400_BAD_REQUEST)

        try:
            nques = int(nques)
            if nques > 40 :
                nques = 40
        except ValueError:
            return Response(status=HTTP_400_BAD_REQUEST)

        random_questions = Question.objects.get_random(mode=mode, course=course, nques=nques)
        serializer = QuestionsSerializer(random_questions, many=True)
        return Response(serializer.data , status=HTTP_200_OK)

class SubmitQuizView(APIView):
    permission_classes = (AllowAny,)
    def post(self , request):
        user = request.user
        data = request.data
        course = data.get('course', None)
        mode = data.get('mode' , None)
        users_answers = data.get('users_answers' , None)

        if course is None or mode is None or users_answers:
            return Response(status=HTTP_400_BAD_REQUEST)

        marked = Question.objects.mark(users_answers=users_answers, course=course, mode=mode)

        if user.is_authenticated:
            pass

        return Response(marked, status=HTTP_200_OK)


class ChallangeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        challangee = request.user
        challanger = data.get('challanger' , None)
        course = data.get('course', None)

        if course is None :
            return Response(status=HTTP_400_BAD_REQUEST)

        # You cant challnage yourself
        if challanger.get('id', None) == challangee :
            return Response(status=HTTP_400_BAD_REQUEST)

        try:
            course_inst = Course.objects.get(title=course.get('title'), id=course.get('id'))
        except Course.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

        try:
            challanger_user = User.objects.get(id=challanger.get('id'), username=challanger.get('username'))
        except User.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

        questions_length = len(Question.objects.all())

        if questions_length >= 5 :
            questions = random.sample(list(Question.objects.filter(course=course_inst)), 5)
        else:
            questions = random.sample(list(Question.objects.filter(course=course_inst)), questions_length)

        serializer = QuestionsSerializer(questions , many=True)

        quiz = {
            "course": course,
            "questions":serializer.data
        }

        try:
            Challange.objects.create(challangee=challangee, challanger=challanger_user,quiz=quiz)
        except Exception as E:
            return Response(status=HTTP_400_BAD_REQUEST)

        return Response(serializer.data , status=HTTP_200_OK)


