from django.views import generic
from .models import SongGroup


class GroupView(generic.DetailView):
    model = SongGroup
    template_name = 'groups/group.html'
    context_object_name = 'group'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{context['group'].name}"
        return context

class GroupListView(generic.ListView):
    model = SongGroup
    template_name = 'groups/groups.html'
    context_object_name = 'groups'
    ordering = ['name']
