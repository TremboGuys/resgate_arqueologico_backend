from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Player
from core.serializers import PlayerSerializer

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all().order_by("-score")
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend]