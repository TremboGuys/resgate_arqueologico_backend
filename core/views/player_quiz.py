from rest_framework.viewsets import ModelViewSet

from core.models import PlayerQuiz
from core.serializers import PlayerQuizSerializer

class PlayerQuizViewSet(ModelViewSet):
    queryset = PlayerQuiz.objects.all()
    serializer_class = PlayerQuizSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)