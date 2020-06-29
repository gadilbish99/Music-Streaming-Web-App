from rest_framework import serializers 
from .models import *

class SongSerializer(serializers.ModelSerializer):
    artist_name = serializers.StringRelatedField(source='artist')
    song_title = serializers.StringRelatedField(source='title')
    song_url = serializers.FileField(source='file')
    img_url = serializers.FileField(source='cover_image')

    class Meta:
        model = Song 
        fields = ('pk', 'song_title','artist_name', 'song_url', 'img_url')

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetail
        exclude = ['user']

class UserSerializer(serializers.ModelSerializer):
    detail = UserDetailSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'detail')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        detail_data = validated_data.pop('detail')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserDetail.objects.create(user=user, **detail_data)
        return user

    def update(self, instance, validated_data):
        detail_data = validated_data.pop('detail')
        detail = instance.detail

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        detail.firstname = detail_data.get('firstname', detail.firstname)
        detail.lastname = detail_data.get('lastname', detail.lastname)
        detail.address = detail_data.get('gender', detail.gender)
        detail.birthdate = detail_data.get('birthdate', detail.birthdate)
        detail.country = detail_data.get('country', detail.country)
        detail.save()

        return instance
