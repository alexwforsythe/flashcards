from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    url(r'^decks/$', views.DeckList.as_view()),
    url(r'^decks/(?P<pk>[0-9]+)/$', views.DeckDetail.as_view()),
    url(r'^decks/(?P<pk>[0-9]+)/cards/$', views.DeckDetail.as_view()),
    url(r'^decks/(?P<dpk>[0-9]+)/cards/(?P<cpk>[0-9]+)/$', views.CardDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
