from datetime import date
from django.db import models
#Create your models here
class Song(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateField(default=date.today)
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Artiste(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    age = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Lyric(models.Model):
    content = models.CharField(max_length=800)
    song = models.ForeignKey('Song', blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content        