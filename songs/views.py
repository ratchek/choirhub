from django.views import generic
from .models import Song

class SongView(generic.DetailView):
    model = Song
    template_name = 'songs/group.html'
    context_object_name = 'song'

class SongListView(generic.ListView):
    model = Song
    template_name = 'songs/groups.html'
    context_object_name = 'songs'
    ordering = ['name']
