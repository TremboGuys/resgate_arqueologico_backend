from django.db import models

from .quiz import Quiz

class Question(models.Model):
    statement = models.CharField(max_length=200)
    alternative_a = models.CharField(max_length=120)
    alternative_b = models.CharField(max_length=120)
    alternative_c = models.CharField(max_length=120)
    alternative_d = models.CharField(max_length=120)
    response = models.CharField(max_length=1)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
