from datetime import date
from musicapp.models import Song, Artiste
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'likes', 'date_published', 'artiste_id']

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'


today= date.today()  # current date


date = today.strftime("%Y-%b-%d")


def validate(self, date):
    return today.strftime("date and time:", date)



