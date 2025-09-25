from rest_framework.viewsets import ModelViewSet
from core.models import Player
from core.serializers import PlayerSerializer

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all().order_by("-xp")
    serializer_class = PlayerSerializer