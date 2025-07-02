from django.db import models

from core.models import Player, Quiz

class PlayerQuiz(models.Model):
    id_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="quizzes")
    id_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="players")
    hits = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [('id_player', 'id_quiz')]
        verbose_name_plural = "Player Quizzes"

    def __str__(self):
        return f"{self.id_player.user.first_name} - {self.id_quiz.theme}"