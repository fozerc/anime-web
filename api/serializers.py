from rest_framework import serializers

from anime_app.models import AnimeModel, CharacterModel


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeModel
        fields = '__all__'


class AnimeCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterModel
        fields = '__all__'
