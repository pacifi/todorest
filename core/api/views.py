"""Modulo View."""

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer


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


