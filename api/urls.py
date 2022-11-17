from django.urls import path
from .views import song_list, song_detail, artiste_list

urlpatterns = [
   path("artiste/", artiste_list, name="artiste_list"),
   path("song/", song_list, name="song_list"),
   path("song/<int:id>/", song_detail, name="song_detail"), 
]