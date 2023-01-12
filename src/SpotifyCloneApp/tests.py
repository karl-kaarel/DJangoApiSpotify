from django.test import TestCase, Client
from django.urls import reverse
from SpotifyCloneApp.models import Playlists
from SpotifyCloneApp.views import SpotifyApi
import json

# Create your tests here.

class TestViews(TestCase):
    def test_GET(self):
        c = Client()
        #ToBeSent
        response = c.get(reverse("playlists"))

        #ToReceive
        self.assertEquals(response.status_code, 200)

    def test_POST_PUT_DELETE(self):
        c = Client()
        data_post = {
            "name":"Tango"
        }
        data_put = {
            "id": 1,
            "name":"Funk"
        }

        #ToBeSent
        response_post = c.post(reverse("playlists"), data_post, content_type="application/json")
        response_get_post = c.get(reverse("playlists"))

        response_put = c.put(reverse("playlists"), data_put, content_type="application/json")
        response_get_put = c.get(reverse("playlists"))

        response_delete = c.delete(reverse("playlists", args=[1]))
        response_get_delete = c.get(reverse("playlists"))

        #ToReceive
        self.assertEquals(response_post.status_code, 200)
        self.assertEquals(response_post.json(), "Added successfuly")

        self.assertEquals(response_get_post.status_code, 200)
        self.assertEquals(response_get_post.json(), {'items': [{'id': 1, 'name': 'Tango'}]})
        print(response_get_post.json())#Tango after post

        self.assertEquals(response_put.status_code, 200)
        self.assertEquals(response_put.json(), "Update successful")

        self.assertEquals(response_get_put.status_code, 200)
        self.assertEquals(response_get_put.json(), {'items': [{'id': 1, 'name': 'Funk'}]})
        print(response_get_put.json())#Funk after update

        self.assertEquals(response_delete.status_code, 200)
        self.assertEquals(response_delete.json(), "Deleted successfuly")

        self.assertEquals(response_get_delete.status_code, 200)
        self.assertEquals(response_get_delete.json(), {'items': []})
        print(response_get_delete.json())#empty after delete
