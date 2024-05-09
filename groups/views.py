from django.views import generic
from .models import SongGroup

class GroupView(generic.DetailView):
    model = SongGroup
    template_name = 'groups/display_group.html'
    context_object_name = 'song_group'

class GroupListView(generic.ListView):
    model = SongGroup
    template_name = 'groups/index.html'
    context_object_name = 'groups'
    ordering = ['name']
