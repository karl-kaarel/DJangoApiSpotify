from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SpotifyCloneApp.models import Playlists
from SpotifyCloneApp.serializers import PlaylistSerializer

# Create your views here.

@csrf_exempt
def SpotifyApi(request, id=0):
    
    if request.method == 'GET':
        playlists = Playlists.objects.all()
        playlists_serializer=PlaylistSerializer(playlists, many=True)
        return JsonResponse(playlists_serializer.data, safe=False)

    elif request.method == 'POST':
        playlist_data = JSONParser().parse(request)
        playlists_serializer = PlaylistSerializer(data=playlist_data)
        if playlists_serializer.is_valid():
            playlists_serializer.save()
            return JsonResponse("Added successfuly", safe=False)
        return JsonResponse("Failed to add", safe=False)

    elif request.method == 'PUT':
        playlist_data = JSONParser().parse(request)
        playlist = Playlists.objects.get(PlaylistId=playlist_data['PlaylistId'])
        playlists_serializer = PlaylistSerializer(playlist, data=playlist_data)
        if playlists_serializer.is_valid():
            playlists_serializer.save()
            return JsonResponse("Update successful", safe=False)
        return JsonResponse("Failed to update")

    elif request.method == 'DELETE':
        playlist = Playlists.objects.get(PlaylistId=id)
        playlist.delete()
        return JsonResponse("Deleted successfuly", safe=False)