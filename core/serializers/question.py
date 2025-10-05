from rest_framework.serializers import ModelSerializer

from core.models import Question

class QuestionRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'statement', 'alternative_a', 'alternative_b', 'alternative_c', 'alternative_d', 'response']

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"