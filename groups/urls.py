from django.urls import path
from .views import SongGroupView, GroupListView

urlpatterns = [
    path('song-group/<int:pk>', SongGroupView.as_view(), name='display_group_songs'),  # Display the songs in a group
    path("", GroupListView.as_view(), name="index"),
]
