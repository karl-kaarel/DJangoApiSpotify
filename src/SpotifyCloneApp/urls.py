from django.urls import re_path
from SpotifyCloneApp import views

handler403 = views.ratelimited_error

urlpatterns=[
    re_path(r'^playlists/$', views.SpotifyApi, name="playlists"),
    re_path(r'^playlists/([0-9]+)$',views.SpotifyApi, name="playlists")
]