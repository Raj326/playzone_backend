from rest_framework import serializers
from .models import Quadra, CentroEsportivo, Reserva


class CentroEsportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroEsportivo
        fields = '__all__'
