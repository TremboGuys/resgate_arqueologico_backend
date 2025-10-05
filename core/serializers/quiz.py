from rest_framework.serializers import ModelSerializer

from core.models import Quiz
from .question import QuestionRetrieveSerializer

class QuizSerializer(ModelSerializer):
    questions = QuestionRetrieveSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = "__all__"

class QuizRetrieveSerializer(ModelSerializer):
    questions = QuestionRetrieveSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = ['id', 'theme', 'xp_per_question', 'image', 'questions']