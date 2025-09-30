from rest_framework.serializers import ModelSerializer

from core.models import Player, PlayerQuiz

class PlayerQuizSerializer(ModelSerializer):
    class Meta:
        model = PlayerQuiz
        fields = fields = ['id', 'player', 'quiz', 'hits', 'score']
    
    def create(self, validated_data):
        player = Player.objects.get(id=validated_data['player'])
        player.score += validated_data['score']
        player.save()
        return super().create(validated_data)