from .serializers import  SongSerializer, ArtisteSerializer
from musicapp.models import Song, Artiste
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND

# Create your views here.
@csrf_exempt
def song_list(request):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
def artiste_list(request):
    if request.method == "GET":
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return JsonResponse(serializer.data, safe=False)        


@csrf_exempt
def song_detail(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return JsonResponse({"message":"Song not found"}, status=HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SongSerializer(song)
        return JsonResponse(serializer.data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SongSerializer(song, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        song.delete()
        return JsonResponse(serializer.data, status=HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def song_list(request):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    elif request.method == "POST":
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def artiste_list(request):
    if request.method == "GET":
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

@api_view(["GET", "PUT", "DELETE"])
def song_detail(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response({"message":"Song not found"}, status=HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        song.delete()
        return Response(status=HTTP_204_NO_CONTENT)