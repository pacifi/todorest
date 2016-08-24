from rest_framework.views import APIView
from rest_framework.response import Response


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
