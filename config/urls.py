from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from usuario.router import router as usuario_router

from core.views import *

router = DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'playerQuizzes', PlayerQuizViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/players/', PlayerViewSet.as_view()),
    path('api/usuarios/', include(usuario_router.urls))
]