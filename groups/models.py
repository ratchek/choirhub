from django.db import models
from songs.models import Song

class SongGroup(models.Model):
    '''
    Model for song groups.
    Each song group has a name (e.g., 'Christmas', 'Easter', 'April 13th concert', etc.)
    and can have multiple songs.
    Used purely for organization purposes
    '''
    name = models.CharField(max_length=255)
    # TODO add owner and choir fields once those apps are working
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='song_groups')
    # choir = models.ForeignKey(Choir, on_delete=models.CASCADE, related_name='song_groups')
    songs = models.ManyToManyField(Song, related_name='song_groups', blank=True) # e.g. Christmas, Easter, April 13th concert, etc.

    def __str__(self):
        return self.name
