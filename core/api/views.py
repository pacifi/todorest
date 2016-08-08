from rest_framework.views import APIView
from rest_framework.response import Response


class HolaMundo(APIView):
    def get(self, request, nombre, format=None):
        print(request.GET.get('papa'))
        return Response({'mensaje': 'Hola Mundo %s' %nombre})
