from .models import Event
# Make sure that the events are available in all views
# needed for navigation
def add_events_to_all_views(request):
    no_of_events_to_display = 5
    return {
        'nav_events': Event.objects.all().order_by('date').reverse()[ : no_of_events_to_display]
    }
