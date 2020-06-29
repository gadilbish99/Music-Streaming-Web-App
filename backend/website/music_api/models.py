from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import FileExtensionValidator
import os,sys

from tinytag import TinyTag

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)

class UserDetail(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='detail'
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    birthdate = models.DateField()
    country = models.CharField(max_length=100)
    joined_date = models.DateField(auto_now_add=True)

class Song(models.Model):
    file = models.FileField(upload_to='music/', validators=[FileExtensionValidator(allowed_extensions=['mp3', 'aac'])])
    title = models.CharField(max_length=100, blank=True)
    artist = models.CharField(max_length=100, blank=True)
    album = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True, null=True)
    cover_image = models.FileField(upload_to='cover_images', blank=True)

    def save(self, *args, **kwargs):
        super(Song, self).save(*args, **kwargs)

        file_path = os.path.join(settings.MEDIA_ROOT, self.file.name)
        tags = TinyTag.get(file_path, image=True)
        
        self.title = tags.title
        self.artist = tags.artist
        self.album = tags.album
        self.year = tags.year

        file_path = os.path.join(settings.MEDIA_ROOT, "cover_images/" + self.album + '.jpg')

        if not os.path.exists(settings.MEDIA_ROOT + "/cover_images"):
            os.mkdir(settings.MEDIA_ROOT + "/cover_images")

        if not os.path.isfile(file_path):
            with open(file_path, "wb") as f:
                f.write(tags.get_image())

        self.cover_image.name = "./cover_images/" + self.album + '.jpg'
        print(self.cover_image)

        super(Song, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)
        return super(Song, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

class FavoriteSongs(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    song = models.ForeignKey(
        Song, 
        on_delete=models.CASCADE
    )
    date_added = models.DateField(auto_now_add=True)

    class Meta(object):
        unique_together = [("user", "song")]