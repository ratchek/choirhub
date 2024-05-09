from django.views import generic
from .models import Event



class EventView(generic.DetailView):
    model = Event
    template_name = 'events/event.html'
    context_object_name = 'event'

class EventListView(generic.ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['name']
