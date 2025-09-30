from django.db import models

from core.models import Player, Quiz

class PlayerQuiz(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="quizzes")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="players")
    hits = models.PositiveSmallIntegerField()
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.player.username} - {self.quiz.theme}"