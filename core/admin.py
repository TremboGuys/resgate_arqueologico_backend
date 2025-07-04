from django.contrib import admin

from core.models import *

admin.site.register(Classroom)
admin.site.register(Player)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(PlayerQuiz)
admin.site.register(PlayerQuestion)