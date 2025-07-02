from rest_framework.viewsets import ModelViewSet

from core.models import Question
from core.serializers import QuestionSerializer, QuestionRetrieveSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return QuestionRetrieveSerializer
        return QuestionSerializer