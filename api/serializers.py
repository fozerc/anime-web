from rest_framework import serializers

from anime_app.models import AnimeModel, CharacterModel, MangaModel, AnimeUser


class AnimeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeUser
        fields = '__all__'

    def create(self, validated_data):
        user = AnimeUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user


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

