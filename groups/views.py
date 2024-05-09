from django.views import generic
from .models import SongGroup

class GroupView(generic.DetailView):
    model = SongGroup
    template_name = 'groups/group.html'
    context_object_name = 'group'

class GroupListView(generic.ListView):
    model = SongGroup
    template_name = 'groups/groups.html'
    context_object_name = 'groups'
    ordering = ['name']
