from .models import Course
from rest_framework.views import APIView
from .serializers import CoursesSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK

# Create your views here.
class RetrieveCoursesView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        data = Course.objects.all()
        serializer = CoursesSerializer(data , many=True)
        return Response(serializer.data, status=HTTP_200_OK)