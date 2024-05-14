from django.contrib import admin
from .models import Song, SongScore, SongRecording, VoiceGroup

class SongScoreInline(admin.TabularInline):
    model = SongScore
    fields = ['file',]
    extra = 1
class SongRecordingInline(admin.TabularInline):
    model = SongRecording
    fields = ['voice_group', 'file',]
    extra = 1

class SongAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        # Set the initial value of the 'owner' field to the current user
        return {'owner': request.user.pk}
    inlines = [SongScoreInline, SongRecordingInline]
# Register your models here.
admin.site.register(Song, SongAdmin)
admin.site.register(SongScore)
admin.site.register(SongRecording)
admin.site.register(VoiceGroup)
