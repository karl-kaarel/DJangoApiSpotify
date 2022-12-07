from rest_framework import serializers
from SpotifyCloneApp.models import Playlists

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = ('PlaylistId', 'PlaylistName')