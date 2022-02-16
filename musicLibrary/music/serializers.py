from dataclasses import fields
from rest_framework import serializers
from .models import Song

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'genre', 'release_date']