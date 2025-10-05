from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class UsuarioRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name', 'email', 'password']

class UsuarioListSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name']