from .models import Song
# Make sure that the groups are available in all views
# needed for navigation
def add_songs_to_all_views(request):
    return {
        'nav_songs': Song.objects.all()
    }
