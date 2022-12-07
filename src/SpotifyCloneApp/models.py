from django.db import models

# Create your models here.

class Playlists(models.Model):
    PlaylistId = models.AutoField(primary_key=True)
    PlaylistName = models.CharField(max_length=500)
