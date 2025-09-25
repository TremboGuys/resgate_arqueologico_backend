from django.db import models

from core.models import Classroom

class Player(models.Model):
    username = models.CharField(max_length=30, unique=True)
    photo_path = models.CharField(max_length=50)
    xp = models.PositiveSmallIntegerField(default=0)
    # id_classroom = models.ForeignKey(Classroom, on_delete=models.PROTECT, related_name="player")

    def __str__(self):
        return f"{self.username} {self.xp}"