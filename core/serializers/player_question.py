from rest_framework.serializers import ModelSerializer

from core.models import PlayerQuestion

class PlayerQuestionSerializer(ModelSerializer):
    class Meta:
        model = PlayerQuestion
        fields = ['id', 'player', 'quiz', 'question', 'hit']
        depth = 1