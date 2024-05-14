from django.urls import path
from .views import index, about, settings

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name="about"),
    path("user-settings", settings, name="user-settings"),
]
