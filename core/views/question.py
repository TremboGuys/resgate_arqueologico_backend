from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Question
from core.serializers import QuestionSerializer, QuestionRetrieveSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    filter_backends = [DjangoFilterBackend]
    fielterset_fields = ['id_quiz__theme']

    def get_serializer_class(self):
        if self.action == "retrieve":
            return QuestionRetrieveSerializer
        return QuestionSerializer