from django.contrib import admin
from django.urls import path, include

from music_api import views
from django.conf.urls import url

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
    path(r'songs/', song_list),
    path(r'favorite_songs/', favorite_songs),
    path(r'favorite_songs_delete/', favorite_songs_delete),
]