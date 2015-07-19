from django.db import models


class Deck(models.Model):
    owner = models.ForeignKey('auth.User', related_name='decks')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=144, blank=True, default='')

    class Meta:
        ordering = ('created', 'title',)


class Card(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    front = models.CharField(max_length=144, blank=True, default='')
    back = models.CharField(max_length=144, blank=True, default='')

    class Meta:
        ordering = ('created',)
