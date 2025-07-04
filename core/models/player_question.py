from django.db import models

from .question import Question
from .quiz import Quiz
from .player import Player

class PlayerQuestion(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="players")
    id_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="players_question")
    id_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="questions")
    hit = models.BooleanField()

    def __str__(self):
        return f"{self.id_player.user.first_name} {self.id_player.user.last_name} - {self.id_question.statement}"
    
    class Meta:
        verbose_name_plural = "Players Question"