from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CentroEsportivoSerializer
from .models import Quadra, CentroEsportivo, Reserva
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})


class CentroEsportivoViewSet(viewsets.ModelViewSet):
    queryset = CentroEsportivo.objects.all()
    serializer_class = CentroEsportivoSerializer


