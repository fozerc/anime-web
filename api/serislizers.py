from django.db.models import Q
from rest_framework import serializers

from mb_characters_app.models import AnimeUser, AnimeModel, CharacterModel, MangaModel, WikiModel, SectionModel, \
    PostModel, Comment, CommentReaction


# class AnimeUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnimeUser
#         fields = '__all__'
#
#     # def create(self, validated_data):
#     #     user = AnimeUser.objects.create_user(
#     #         username=validated_data['username'],
#     #         password=validated_data['password']
#     #     )
#     #     return user
#
#     def validate(self, attrs):
#         username = attrs.get('username')
#         email = attrs.get('email')
#         user_exist = Q(username__iexact=username) | Q(email__iexact=email)
#         if AnimeUser.objects.filter(user_exist).count():
#             raise serializers.ValidationError()
#         return attrs


class AnimeUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AnimeUser
        fields = ('username', 'password', 'id')

    def create(self, validated_data):
        user = AnimeUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
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


class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiModel
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionModel
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentsReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReaction
        fields = '__all__'
