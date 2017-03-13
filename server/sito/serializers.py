from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sito.models import Sportivo, Attivita, Risultato, Test

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email')

class SportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sportivo
        fields = ('id','nome', 'cognome', 'sport', 'data_nascita', 'luogo_nascita', 'paese_nascita', 'altezza', 'peso', 'foto')

class AttivitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attivita
        fields = ('id', 'nome', 'descrizione', 'numEvento', 'giornoEvento', 'annoEvento', 'meseEvento', 'prezzo', 'sconto', 'facilitazioni', 'organizzatore', 'created')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'nome')