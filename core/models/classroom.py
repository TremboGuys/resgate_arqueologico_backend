from django.db import models

class Classroom(models.Model):
    nome = models.CharField(max_length=7, unique=True)