from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.views import *

router = DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'playerQuizzes', PlayerQuizViewSet)
router.register(r'playerQuestions', PlayerQuestionViewset)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]