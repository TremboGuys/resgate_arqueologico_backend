from rest_framework.serializers import ModelSerializer

from core.models import PlayerQuiz

class PlayerQuizSerializer(ModelSerializer):
    class Meta:
        model = PlayerQuiz
        fields = fields = ['id', 'player', 'quiz', 'hits']