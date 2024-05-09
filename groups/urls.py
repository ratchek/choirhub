from django.urls import path
from .views import GroupView, GroupListView

urlpatterns = [
    path('song-group/<int:pk>', GroupView.as_view(), name='display_group_songs'),  # Display the songs in a group
    path("", GroupListView.as_view(), name="index"),
]
