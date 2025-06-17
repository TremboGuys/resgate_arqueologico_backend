from rest_framework import serializers

from core.models import Player

from usuario.models import Usuario
from usuario.serializers import UsuarioSerializer, UsuarioRetrieveSerializer, UsuarioListSerializer

class PlayerSerializer(serializers.ModelSerializer):
    user_details = UsuarioRetrieveSerializer(source='user', read_only=True)

    class Meta:
        model = Player
        fields = ['user_details', 'xp', 'id_classroom']

class PlayerListSerializer(serializers.ModelSerializer):
    user_details = UsuarioListSerializer(source='user', read_only=True)

    class Meta:
        model = Player
        fields = ['user_details', 'xp', 'id_classroom']
        depth = 1