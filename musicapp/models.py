import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    age = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_published = models.DateField(default=datetime.date.today)
    likes = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=4000)

    def __str__(self):
        return self.content
   
    
