from .models import Event
# Make sure that the events are available in all views
# needed for navigation
def add_events_to_all_views(request):
    return {
        'nav_events': Event.objects.all().order_by('date')
    }
