from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.db.models import Value, IntegerField, Window, F
from django.db.models.functions import RowNumber

from core.models import PlayerQuiz
from core.serializers import PlayerQuizSerializer, PlayerQuizListSerializer

class PlayerQuizViewSet(ModelViewSet):
    queryset = PlayerQuiz.objects.all().order_by("-score")
    serializer_class = PlayerQuizSerializer

    def list(self, request, *args, **kwargs):
        quiz = request.GET.get('quiz', None)
        player = int(request.GET.get('player', None))

        if quiz is not None:
            query = PlayerQuiz.objects.filter(quiz=quiz).annotate(position=Window(expression=RowNumber(), partition_by=[F("quiz")], order_by=[F("score").desc(), F("id").asc()])).order_by("position")
            if query.exists():
                    position_player = 0
                    for q in query:
                        if (q.player.id == player):
                            position_player = q.position
                    if position_player > 10:
                        query = query.filter(position__lte=10) | query.filter(player=player)
                    else:
                        query = query.filter(position__lte=10)
                    serializer = PlayerQuizListSerializer(query, many=True)
            else:
                return Response(data=[], status=status.HTTP_204_NO_CONTENT)
        else:
            query = self.queryset

            serializer = PlayerQuizListSerializer(query, many=True)

        
        return Response({"ranking": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)