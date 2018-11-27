from rest_framework import serializers
from .models import Constructora, Edificio, Apartamento

class ConstructoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Constructora
        fields = ('__all__')


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = ('__all__')

class ApartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apartamento
        fields = ('__all__')