from django.contrib import admin
from .models import Song, SongScore, SongRecording, VoiceGroup

# Register your models here.
admin.site.register(Song)
admin.site.register(SongScore)
admin.site.register(SongRecording)
admin.site.register(VoiceGroup)
