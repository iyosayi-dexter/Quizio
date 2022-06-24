from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Lesson
from .serializers import LessonListSeriaizer, LessonDetailSerializer
from rest_framework.status import HTTP_200_OK , HTTP_404_NOT_FOUND
from rest_framework.response import Response


class LessonRetrieveView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Lesson.objects.all().order_by('-date_created')
    serializer_class = LessonListSeriaizer

class LessonDetailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, slug):
        try:
            queryset = Lesson.objects.get(slug=slug)
            serializer = LessonDetailSerializer(queryset)
            return Response(serializer.data, status=HTTP_200_OK)
        except Lesson.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


