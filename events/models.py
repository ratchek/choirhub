from django.db import models
from django.conf import settings
from songs.models import Song
# from choirs.models import Choir

class Event(models.Model):
    '''
    Model for events.
    Each event has a name, date, time, and location.
    Each event can have multiple songs.
    Each event can belong to a single choir (TODO)
    '''
    name = models.CharField(max_length=255)
    # choir = models.ForeignKey(Choir, on_delete=models.CASCADE, related_name='events', null=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    songs = models.ManyToManyField(Song, related_name='events', blank=True) # songs that will be performed at the event
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserEventStatus(models.Model):
    '''
    Model for user statuses for events.
    For each event a user can declare whether they are going to attend, can't attend, or are undecided.
    After the event, the user's actual attendance is recorded.
    '''

    # TODO: Don't allow user to change this after the event has passed
    class AttendanceDeclaration(models.TextChoices):
        ''' What a user can pick as their status for an upcoming event.'''
        GOING_TO_ATTEND = 'Going', 'Going to attend'
        CANT_ATTEND = 'Cant', "Can't attend"
        DONT_KNOW = 'Undecided', "Don't know" # user hasn't decided yet. This is an option a user can pick
        NOT_DECLARED = 'Undeclared', 'Not declared' # user hasn't picked any option yet

    class ActualAttendance(models.TextChoices):
        ''' Whether or not a user attended an event. Can't be changed by the user.'''
        ATTENDED = 'Present', 'Attended'
        DIDNT_ATTEND = 'Absent', "Didn't attend"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='event_statuses')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='user_statuses')
    declaration = models.CharField(max_length=20, choices=AttendanceDeclaration.choices, default=AttendanceDeclaration.NOT_DECLARED, verbose_name='Attendance declaration')
    actual_attendance = models.CharField(max_length=20, choices=ActualAttendance.choices, blank=True, null=True, verbose_name='Actual attendance')

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user} - {self.event} - {self.declaration}"
