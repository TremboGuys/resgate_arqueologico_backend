from rest_framework.serializers import ModelSerializer

from core.models import PlayerQuiz
from core.serializers import QuizRetrieveSerializer

class PlayerQuizSerializer(ModelSerializer):
    class Meta:
        model = PlayerQuiz
        fields = "__all__"
        depth = 1