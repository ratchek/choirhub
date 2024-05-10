from typing import Any
from django.views import generic
from .models import Event



class EventView(generic.DetailView):
    model = Event
    template_name = 'events/event.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{context['event'].name}"
        return context

class EventListView(generic.ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['name']
