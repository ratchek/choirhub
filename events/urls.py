from django.urls import path
from .views import EventView, EventListView

urlpatterns = [
    path('/<int:pk>', EventView.as_view(), name='event-detail'),
    path("/", EventListView.as_view(), name="event-list"),
]
