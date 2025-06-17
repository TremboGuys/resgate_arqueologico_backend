from rest_framework.viewsets import ModelViewSet

from core.models import Player
from core.serializers import PlayerSerializer

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer