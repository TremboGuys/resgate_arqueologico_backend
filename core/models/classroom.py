from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.name