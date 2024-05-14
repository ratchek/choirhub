from django.views import generic
from .models import Song
import logging
from django.contrib.auth.mixins import LoginRequiredMixin


logger = logging.getLogger(__name__)

class SongView(LoginRequiredMixin, generic.DetailView):
    model = Song
    template_name = 'songs/song.html'
    context_object_name = 'song'

class SongListView(LoginRequiredMixin, generic.ListView):
    model = Song
    template_name = 'songs/songs.html'
    context_object_name = 'songs'
    ordering = ['title']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All songs"
        return context
