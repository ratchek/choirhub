from django.contrib import admin
from .models import Song, SongScore, SongRecording, VoiceGroup

class SongScoreInline(admin.TabularInline):
    model = SongScore
    fields = ['file',]
    extra = 1

class SongAdmin(admin.ModelAdmin):
    inlines = [SongScoreInline]

# Register your models here.
admin.site.register(Song, SongAdmin)
admin.site.register(SongScore)
admin.site.register(SongRecording)
admin.site.register(VoiceGroup)
