from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from core.models import PlayerQuestion
from core.serializers import PlayerQuestionSerializer

class PlayerQuestionViewset(ModelViewSet):
    queryset = PlayerQuestion.objects.all()
    serializer_class = PlayerQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_player', 'id_quiz']