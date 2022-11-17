import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    age = models.IntegerField(default=1)
    song = models.ForeignKey('Song', blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Song(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateField(default=datetime.date.today)
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length=20)
    lyric = models.ForeignKey('Lyric', blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    
    

class Lyric(models.Model):
    content = models.CharField(max_length=800)
    song_id = models.CharField(max_length=20)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    