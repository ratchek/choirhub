from django.urls import path
from .views import SongGroupView

urlpatterns = [
    path('', SongGroupView.as_view(), name='base'),  # add this line
]
