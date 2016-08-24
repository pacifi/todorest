"""Modulo User Serializer"""

from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import ToDo

class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer.

    Metodo para serializer, interpreta los modelos y los convierte en
    en xml o json para nuestro caso es un json.
    """

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")
        write_only_fields = ("password",)


class ToDoSerializer(serializers.ModelSerializer):
    """
    Todo Serializer.

    Serializer para enviar json del modelo Todo.
    """

    class Meta:
        model = ToDo
        fields = ("id", "fecha_creado", "fecha_finalizado", "fecha_finalizado", "todo", "hecho")

