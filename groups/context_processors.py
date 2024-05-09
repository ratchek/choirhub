from .models import SongGroup
# Make sure that the groups are available in all views
# needed for navigation
def add_song_groups_to_all_views(request):
    return {
        'nav_groups': SongGroup.objects.all()
    }
