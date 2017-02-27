from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sito.models import Sportivo, Attivita, Risultato, Test

class UserSerializer(serializers.ModelSerializer):
    sportivi = serializers.HyperlinkedRelatedField(queryset=Sportivo.objects.all(), view_name='sportivo-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'sportivi')

class SportivoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Sportivo
        fields = ('id','nome', 'cognome', 'data_nascita', 'luogo_nascita', 'paese_nascita', 'altezza', 'peso', 'foto', 'owner')

class AttivitaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Attivita
        fields = ('id', 'nome', 'descrizione', 'data', 'prezzo', 'sconto', 'facilitazioni', 'organizzatore', 'created', 'owner')

class TestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Test
        fields = ('id', 'nome', 'owner')