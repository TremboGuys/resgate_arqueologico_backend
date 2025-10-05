from rest_framework.serializers import ModelSerializer

from core.models import PlayerQuestion

class PlayerQuestionSerializer(ModelSerializer):
    class Meta:
        model = PlayerQuestion
        fields = ['id', 'player', 'quiz', 'question', 'hit']

    def create(self, validated_data):
        pq = PlayerQuestion.objects.filter(player=validated_data['player'].id, question=validated_data['question'].id)

        if pq.exists():
            response = self.update(instance=pq.first(), validated_data=validated_data)
            return response
        return super().create(validated_data)