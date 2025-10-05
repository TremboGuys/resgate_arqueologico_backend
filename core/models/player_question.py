from django.db import models

from .question import Question
from .quiz import Quiz
from .player import Player

class PlayerQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="players")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="players_question")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="questions")
    hit = models.BooleanField()

    def __str__(self):
        return f"{self.player.username} - {self.question.statement}"
    
    class Meta:
        unique_together = [('id_question', 'id_quiz', 'id_player', 'hit')]
        verbose_name_plural = "Players Question"