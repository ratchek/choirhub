from django.urls import path
from .views import SongView, SongListView

urlpatterns = [
    path('<int:pk>', SongView.as_view(), name='song-detail'),
    path("", SongListView.as_view(), name="song-list"),
]
