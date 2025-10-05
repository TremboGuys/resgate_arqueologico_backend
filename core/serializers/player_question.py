from rest_framework.serializers import ModelSerializer

from core.models import PlayerQuestion

class PlayerQuestionSerializer(ModelSerializer):
    class Meta:
        model = PlayerQuestion
        fields = "__all__"
        # depth = 1