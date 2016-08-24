"""Modulo User Serializer"""

from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer.

    Metodo para serializer, interpreta los modelos y los convierte en
    en xml o json para nuestro caso es un json.
    """

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")
