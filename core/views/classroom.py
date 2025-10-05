from rest_framework.viewsets import ModelViewSet

from core.models import Classroom
from core.serializers import ClassroomSerializer

class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer