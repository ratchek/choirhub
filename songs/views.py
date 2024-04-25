from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import SongGroup

class SongGroupView(View):
    def get(self, request, pk,  *args, **kwargs):
        songs = SongGroup.objects.get(pk=pk).songs.all() # fetch all songs from the database
        print(SongGroup.objects.get(pk=pk).songs.all())
        return render(request, 'songs/display_group_songs.html', {'songs': songs})  # pass the songs to the template

class GroupListView(generic.ListView):
    model = SongGroup
    template_name = 'songs/index.html'
    context_object_name = 'groups'
    ordering = ['name']
