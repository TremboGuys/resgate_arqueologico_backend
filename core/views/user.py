from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from core.serializers import UserSerializer, UserListSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return UserListSerializer
        else:
            UserSerializer