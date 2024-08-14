from rest_framework import serializers

from anime_app.models import AnimeModel, CharacterModel, MangaModel


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeModel
        fields = '__all__'


class AnimeCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterModel
        fields = '__all__'


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaModel
        fields = '__all__'

