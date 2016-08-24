"""Modulo View."""

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer, ToDoSerializer

from ..models import ToDo


class HolaMundo(APIView):
    def get(self, request, nombre, format=None):
        """
        Get.

        get(self, request, "NOMBRE", format=None)
        El NOMBRE que recibes es el mismo parametro de entrada que vienes por,
        la url
        """
        # print(request.GET.get('papa'))
        return Response({'mensaje': 'Hola Mundo'})


class UsuarioApi(APIView):
    """
    Usuario Api.

    Este clase sirve un api de los usuarios.
    """

    serializer_class = UserSerializer

    def get(self, request, id=None,format=None):

        if id !=None:
            # users = User.objects.filter(id=id).first()
            users = get_object_or_404(User, pk=id)
            many = False
        else:
            users = User.objects.all()
            many = True

        response = self.serializer_class(users, many=many)
        return Response(response.data)

class ToDoView(APIView):
    """
    Todo View.

    verbos:
        GET (obtiene 1 o muchos objetos)
        POST (Crea 1 o muchos objetos)
        PUT, PATCH (Modifica Objetos)
        DELETE (Elimina 1 o mas objetos)
    """
    serializer_class = ToDoSerializer

    def get(self, request,id=None, format=None):
        todos = ToDo.objects.all()
        response = self.serializer_class(todos, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        todo = self.serializer_class(data=request.data)

        # request.DATA deprecated usage request.data ver: rest_framework 3.2
        if todo.is_valid():
            todo.save(propietario=request.user)
            return Response(todo.data, status=status.HTTP_201_CREATED)
        else:
            return Response(todo.errors, status=status.HTTP_400_BAD_REQUEST)

