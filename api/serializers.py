from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Deck, Card


class UserSerializer(serializers.ModelSerializer):
    decks = serializers.PrimaryKeyRelatedField(many=True, queryset=Deck.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'decks')


class DeckSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Deck
        fields = ('id', 'owner', 'title', 'description')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'front', 'back')
