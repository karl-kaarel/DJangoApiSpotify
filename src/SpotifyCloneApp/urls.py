from django.urls import re_path
from SpotifyCloneApp import views

urlpatterns=[
    re_path(r'^playlists$', views.SpotifyApi),
    re_path(r'^playlists/([0-9]+)$',views.SpotifyApi)
]