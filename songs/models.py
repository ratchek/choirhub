from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

# used for converting pdf to image
from pdf2image import convert_from_bytes
from django.core.files import File
from io import BytesIO

class Song(models.Model):
    title = models.CharField(max_length=255)
    # TODO add owner and choir fields once those apps are working
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='songs')
    # choir = models.ForeignKey(Choir, on_delete=models.CASCADE, related_name='songs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

def song_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/songs/<song.title>/<filename>
    return f'songs/{instance.song.title}/{filename}'

class SongScore(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='scores')
    # TODO add user folders once user auth is implemented
    # TODO add a custom validator to ensure that the file is a PDF (not just using extensions)
    file = models.FileField(upload_to=song_directory_path, validators=[FileExtensionValidator( ['pdf'] ) ])
    img = models.ImageField(upload_to=song_directory_path, blank=True)  # image representation of the score

    def __str__(self):
        return f"{self.song.title} - score"

    # override the save method to create an image from the uploaded PDF
    def save(self, *args, **kwargs):
        self.img = create_img_from_pdf(self.file)  # create an image from the uploaded PDF file
        super().save(*args, **kwargs)  # Call the "real" save() method.


class SongRecording(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='recordings')
    voice_group = models.ForeignKey('VoiceGroup', on_delete=models.CASCADE, related_name='recordings', null=True)
    # TODO add support for wav files? (make sure that they're playable in browser)
    file = models.FileField(upload_to=song_directory_path, validators=[FileExtensionValidator( ['mp3', 'wav'] ) ])

    def __str__(self):
        return f"{self.song.title} - {self.voice_group} - recording"

class VoiceGroup(models.Model):
    name = models.CharField(max_length=50)  # e.g., 'soprano', 'alto', 'tenor', 'bass', 'men', 'women', 'group 1', 'group 2'

    def __str__(self):
        return self.name

class SongGroup(models.Model):
    name = models.CharField(max_length=255)
    # TODO add owner and choir fields once those apps are working
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='song_groups')
    # choir = models.ForeignKey(Choir, on_delete=models.CASCADE, related_name='song_groups')
    songs = models.ManyToManyField(Song, related_name='song_groups', blank=True) # e.g. Christmas, Easter, April 13th concert, etc.

    def __str__(self):
        return self.name

### Helper functions ###
def create_img_from_pdf(pdf):
    """Creates an image of the first page of the pdf"""
    images = convert_from_bytes(pdf.read(), size=(550,None))  # holds all the pages as an array of Pil images
    img_io = BytesIO()  # needed as an intemediary to save the file from Pillow library
    images[0].save(img_io, "WEBP", quality=70)  # save image to BytesIO object
    img = File(img_io, name=pdf.name[:-4] + ".webp")  # create a django friendly File object
    return img
