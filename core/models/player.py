from django.db import models

from usuario.models import Usuario

from core.models import Classroom

class Player(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.PROTECT)
    xp = models.PositiveSmallIntegerField()
    id_classroom = models.ForeignKey(Classroom, on_delete=models.PROTECT, related_name="player")