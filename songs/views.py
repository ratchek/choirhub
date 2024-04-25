from django.shortcuts import render
from django.views import View
from .models import Song

class SongGroupView(View):
    def get(self, request, *args, **kwargs):
        songs = Song.objects.all()  # fetch all songs from the database
        return render(request, 'songs/index.html', {'songs': songs})  # pass the songs to the template
