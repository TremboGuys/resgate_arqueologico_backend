from rest_framework import serializers

from core.models import Player

from usuario.serializers import UsuarioSerializer

class PlayerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True)
    first_name = serializers.CharField(write_only = True)
    last_name = serializers.CharField(write_only = True)

    class Meta:
        model = Player
        fields = ['id_classroom']
    
    def create(self, validated_data):
        classroom = validated_data.pop('id_classroom')

        user_serializer = UsuarioSerializer(data=validated_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        player_data = {"user": user.id, "xp": 0, "id_classroom": classroom}

        Player.objects.create(player_data)

        return super().create(validated_data)