from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField, IntegerField

from core.models import Player, PlayerQuiz

class PlayerQuizSerializer(ModelSerializer):
    class Meta:
        model = PlayerQuiz
        fields = ['id', 'player', 'quiz', 'hits', 'score']
    
    def create(self, validated_data):
        player = Player.objects.get(id=validated_data['player'].id)
        pq = PlayerQuiz.objects.filter(player=player, quiz=validated_data['quiz']).first()

        print(player.score)

        if pq:
            response = self.update(instance=pq, validated_data=validated_data)
            return response
        player.score += validated_data['score']
        player.save()
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        player = Player.objects.get(id=validated_data['player'].id)
        print(validated_data['score'], instance.player.score)
        player.score += validated_data['score'] - instance.player.score
        player.save()

        return super().update(instance, validated_data)
    
class PlayerQuizListSerializer(ModelSerializer):
    username = SerializerMethodField()
    photo = SerializerMethodField()
    position = IntegerField()
    class Meta:
        model = PlayerQuiz
        fields = ['username', 'photo', 'score', 'hits', 'position']

    def get_username(self, obj):
        return obj.player.username
    
    def get_photo(self, obj):
        return obj.player.photo_path