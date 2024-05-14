from django.views import generic
from .models import SongGroup
import logging
from django.contrib.auth.mixins import LoginRequiredMixin

logger = logging.getLogger(__name__)


class GroupView(LoginRequiredMixin, generic.DetailView):
    model = SongGroup
    template_name = 'groups/group.html'
    context_object_name = 'group'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{context['group'].name}"
        context['object_type'] = 'Group'
        logger.debug(context)
        return context

class GroupListView(LoginRequiredMixin, generic.ListView):
    model = SongGroup
    template_name = 'groups/groups.html'
    context_object_name = 'groups'
    ordering = ['name']
