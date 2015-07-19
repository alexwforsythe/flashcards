from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^decks/$', views.deck_list),
    url(r'^decks/(?P<pk>[0-9]+)/$', views.deck_detail),
    url(r'^decks/(?P<pk>[0-9]+)/cards/$', views.deck_detail),
    url(r'^decks/(?P<dpk>[0-9]+)/cards/(?P<cpk>[0-9]+)/$', views.card_detail)
]
