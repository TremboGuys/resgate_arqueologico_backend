from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Quiz
from core.serializers import QuizSerializer, QuizRetrieveSerializer

class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['theme']

    def get_serializer_class(self):
        if self.action == "retrieve":
            return QuizRetrieveSerializer
        return QuizSerializer