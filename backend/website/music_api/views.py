from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import * 
from .serializers import *

from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        songs = Song.objects.filter(title__startswith=request.data["query"])
        serializer = SongSerializer(songs, many=True, context={'request': request})
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def favorite_songs(request):
    user = request.user
    if request.method == 'GET':
        song_list = FavoriteSongs.objects.filter(user=user.id).values_list('song', flat=True)
        favoriteSongs = Song.objects.filter(id__in=song_list)
        serializer = SongSerializer(favoriteSongs, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        song = Song.objects.filter(id=request.data["id"])
        if not FavoriteSongs.objects.filter(user=user, song=song[0]):
            songs = FavoriteSongs.objects.create(user=user, song=song[0])
            serializer = SongSerializer(song, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'This query exists.'})

@api_view(['POST'])
def favorite_songs_delete(request):
    if request.method == 'POST':
        song = Song.objects.filter(id=request.data["id"])
        print(song)
        if FavoriteSongs.objects.filter(user=request.user, song=song[0]):
            FavoriteSongs.objects.filter(user=request.user, song=song[0]).delete()
            return Response({'message': 'Removed'})
        else:
            return Response({'message': 'Error'})
        

from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.permissions import AllowAny
from website.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(id=self.request.user.id)
        return queryset

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

