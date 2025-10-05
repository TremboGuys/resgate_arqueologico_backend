from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter

from core.views import *

router = DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'playerQuizzes', PlayerQuizViewSet, basename="playerQuiz")
router.register(r'playerQuestions', PlayerQuestionViewset)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]