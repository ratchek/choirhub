from django.urls import path
from .views import GroupView, GroupListView

urlpatterns = [
    path('group/<int:pk>', GroupView.as_view(), name='group-detail'),
    path("", GroupListView.as_view(), name="index"),
]
