from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^decks/$', views.deck_list),
    url(r'^decks/(?P<pk>[0-9]+)/$', views.deck_detail)
]
