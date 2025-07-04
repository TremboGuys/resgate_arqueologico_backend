from rest_framework.viewsets import ModelViewSet

from core.models import Quiz
from core.serializers import QuizSerializer, QuizRetrieveSerializer

class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return QuizRetrieveSerializer
        return QuizSerializer