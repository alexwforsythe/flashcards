from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions

from api.models import Deck, Card
from api.serializers import DeckSerializer, UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeckList(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = Deck
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = Card
