from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Player
from core.serializers import PlayerSerializer, PlayerListSerializer

from usuario.serializers import UsuarioSerializer
from usuario.models import Usuario

class PlayerViewSet(APIView):
    def post(self, request):
        user_data = {
            "email": request.data.pop('email'),
            "password": request.data.pop('password'),
            "first_name": request.data.pop('first_name'),
            "last_name": request.data.pop('last_name')
        }

        user_serializer = UsuarioSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = Usuario.objects.create_user(user_data.pop('email'), user_data.pop('password'), **user_data)

        print(user.id)

        player_serializer = PlayerSerializer(data=request.data)
        player_serializer.is_valid(raise_exception=True)
        player_data = player_serializer.save(user=user)

        print(player_data)

        return Response({"message": "Player created with success", "data": PlayerSerializer(player_data).data}, status=status.HTTP_201_CREATED)
    
    def get(self, request, pk=None):
        if pk == None:
            players = Player.objects.all()
            serializer = PlayerListSerializer(players, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            player = Player.objects.get(id=pk)
            serializer = PlayerSerializer(player)
            return Response(serializer.data, status=status.HTTP_200_OK)