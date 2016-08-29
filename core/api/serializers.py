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

    propietario = UserSerializer(many=False, read_only=True)
    # el many se agrega por que el propietari a listar solo es uno
    # el readonly se agrega por que es de lectura en una fase y nos permite
    # pasar el serializer valid para cargar el propietario directamente en el
    # backend con request.user despues de valid.

    class Meta:
        model = ToDo
        fields = ("id", "fecha_creado", "fecha_finalizado", "fecha_finalizado", "todo", "hecho", "propietario")
        # read_only_fields = ("propietario",) # esto se cambia por el read_only de el UserSerializer



class TodoHyperSerializer(serializers.HyperlinkedModelSerializer):

    propietario = serializers.HyperlinkedRelatedField(
        view_name= 'usuario',
        lookup_field='id',
        many=False,
        read_only=True
    )
    class Meta:
        model = ToDo
        fields = ("id", "fecha_creado", "fecha_finalizado", "fecha_finalizado", "todo", "hecho", "propietario")
        read_only_fields = ("propietario",)
