from django.db.models import Q
from rest_framework import serializers

from mb_characters_app.models import AnimeUser, AnimeModel, CharacterModel, MangaModel


class AnimeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeUser
        fields = '__all__'

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        user_exist = Q(username__iexact=username) | Q(email__iexact=email)
        if AnimeUser.objects.filter(user_exist).count():
            raise serializers.ValidationError()
        return attrs


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
