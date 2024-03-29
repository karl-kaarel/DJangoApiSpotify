from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django_ratelimit.decorators import ratelimit
# from django_ratelimit.exceptions import Ratelimited

from SpotifyCloneApp.models import Playlists
from SpotifyCloneApp.serializers import PlaylistSerializer

# Create your views here.

def ratelimited_error(request, exception):
    # or other types:
    return JsonResponse({'error': 'Sorry, too many requests'}, status=429)

@csrf_exempt
@ratelimit(key='user', rate='2/m')
def SpotifyApi(request, PlaylistId=0):
    
    if request.method == 'GET':
        playlists = Playlists.objects.all()
        playlists_serializer=PlaylistSerializer(playlists, many=True)
        return JsonResponse({'items': playlists_serializer.data}, safe=False)

    elif request.method == 'POST':
        playlist_data = JSONParser().parse(request)
        playlists_serializer = PlaylistSerializer(data=playlist_data)
        if playlists_serializer.is_valid():
            playlists_serializer.save()
            return JsonResponse("Added successfuly", safe=False)
        return JsonResponse("Failed to add", safe=False)

    elif request.method == 'PUT':
        playlist_data = JSONParser().parse(request)
        playlist = Playlists.objects.get(id=playlist_data['id'])
        playlists_serializer = PlaylistSerializer(playlist, data=playlist_data)
        if playlists_serializer.is_valid():
            playlists_serializer.save()
            return JsonResponse("Update successful", safe=False)
        return JsonResponse("Failed to update")

    elif request.method == 'DELETE':
        playlist = Playlists.objects.get(id=PlaylistId)
        playlist.delete()
        return JsonResponse("Deleted successfuly", safe=False)