from django.db import models

class Quiz(models.Model):
    theme = models.CharField(max_length=30)
    xp_per_question = models.PositiveSmallIntegerField()
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.theme