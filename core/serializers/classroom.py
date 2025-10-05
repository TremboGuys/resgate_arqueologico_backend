from rest_framework.serializers import ModelSerializer

from core.models import Classroom

class ClassroomSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"