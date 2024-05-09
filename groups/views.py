from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views import generic
from .models import SongGroup

class SongGroupView(View):
    def get(self, request, pk,  *args, **kwargs):
        song_group = get_object_or_404(SongGroup, pk=pk) # fetch the song group from the database
        songs = song_group.songs.all() # fetch all songs in that group
        print (songs)
        return render(request, 'groups/display_group_songs.html', {'songs': songs}) # pass the songs to the template

class GroupListView(generic.ListView):
    model = SongGroup
    template_name = 'groups/index.html'
    context_object_name = 'groups'
    ordering = ['name']
