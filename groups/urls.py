from django.urls import path
from .views import GroupSongsView, GroupListView

urlpatterns = [
    path('song-group/<int:pk>', GroupSongsView.as_view(), name='display_group_songs'),  # Display the songs in a group
    path("", GroupListView.as_view(), name="index"),
]
