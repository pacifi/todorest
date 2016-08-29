"""Modulo View."""

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from rest_framework import status, viewsets, permissions, filters
from rest_framework.filters import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response

from core.api.serializers import TodoHyperSerializer
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

        ==>
    """
    serializer_class = ToDoSerializer
    # serializer_class = TodoHyperSerializer
    # el hyperlink recibe un kwargs

    def get(self, request,id=None, format=None):
        todos = ToDo.objects.all()
        response = self.serializer_class(todos, many=True) # Model Serializer
        # response = self.serializer_class(todos, many=True, context={'request':request}) # HyperLink Serializer
        # el hyperlink recibe un kwargs
        return Response(response.data)

    def post(self, request, format=None):

        todo = self.serializer_class(data=request.data) # modelSerializer
        #  todo = self.serializer_class(data=request.data, context={'request':request})

        # request.DATA deprecated usage request.data ver: rest_framework 3.2
        if todo.is_valid():
            todo.save(propietario=request.user)
            return Response(todo.data, status=status.HTTP_201_CREATED)
        else:
            return Response(todo.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet.
        GET (obtiene 1 o muchos objetos)
        ==> list(lista los objetos)
        ==> retrive(lista un objeto)
        POST (Crea 1 o muchos objetos)
        ==>create (crea un objeto mendiante un post)
        PUT, PATCH (Modifica Objetos)
        ==> update (actualiza un objeto)
        ==> partial_update (path: actualiza un objeto pero solo con los campos que enviamos.
        DELETE (Elimina 1 o mas objetos)
        ==> destroy(borra un objeto
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    # lookup_field = "id"  # lookup_field para filtrar el id que esta entrando en nuevas versiones no es necesario


class ToDoViewSet(viewsets.ModelViewSet):
    """
    Hechos.

    Hechos Rest.
    """
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    # lookup_field = "id"  # ya no se usa
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_backends = (DjangoFilterBackend, filters.Se)



    def list(self, request, *args, **kwargs):
        print(request.user)
        return super(ToDoViewSet, self).list(request, *args, **kwargs)


