from itertools import chain
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsOwnerOrReadOnly
from api.serislizers import AnimeUserSerializer, AnimeSerializer, AnimeCharacterSerializer, MangaSerializer, \
    WikiSerializer, PostSerializer, SectionSerializer, CommentSerializer
from mb_characters_app.models import AnimeUser, AnimeModel, CharacterModel, MangaModel, WikiModel, PostModel, \
    SectionModel, Comment, CommentReaction
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class AnimeUserRegistration(CreateAPIView):
    serializer_class = AnimeUserSerializer
    queryset = AnimeUser.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = AnimeUser.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'Token': token.key}, status=status.HTTP_201_CREATED)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"details": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"details": "Token not found."}, status=status.HTTP_404_NOT_FOUND)


class AnimeModelViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, ]
    serializer_class = AnimeSerializer
    queryset = AnimeModel.objects.all()
    permission_classes = []


class CharacterModelViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, ]
    serializer_class = AnimeCharacterSerializer
    queryset = CharacterModel.objects.all()
    permission_classes = []


class MangaModelViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, ]
    serializer_class = MangaSerializer
    queryset = MangaModel.objects.all()
    permission_classes = []


class GlobalSearchListAPIView(ListAPIView):
    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        if not query:
            return []

        anime = AnimeModel.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        mangas = MangaModel.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        characters = CharacterModel.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

        results = list(chain(anime, mangas, characters))
        return results

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"What are you looking for is not here"}, status=status.HTTP_404_NOT_FOUND)
        results = self.get_serializers(queryset)
        return Response(results)

    def get_serializers(self, queryset):
        results = []
        for obj in queryset:
            if isinstance(obj, AnimeModel):
                serializer = AnimeSerializer(obj)
            elif isinstance(obj, CharacterModel):
                serializer = AnimeCharacterSerializer(obj)
            elif isinstance(obj, MangaModel):
                serializer = MangaSerializer(obj)
            results.append(serializer.data)
        return results


class WikiModelViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, ]
    serializer_class = WikiSerializer
    permission_classes = []
    queryset = WikiModel.objects.all()


class PostModelViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser]
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = PostModel.objects.all()


class SectionModelViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser]
    serializer_class = SectionSerializer
    permission_classes = [AllowAny, IsOwnerOrReadOnly]
    queryset = SectionModel.objects.all()


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None, url_path='like'):
        comment = self.get_object()
        reaction, created = CommentReaction.objects.get_or_create(
            comment=comment, user=request.user
        )
        if reaction.is_like:
            reaction.delete()
            return Response({"details": "Like has been removed"}, status=status.HTTP_200_OK)
        else:
            reaction.is_like = True
            reaction.save()
            return Response({"details": "Like has been added"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None, url_path='dislike'):
        comment = self.get_object()
        reaction, created = CommentReaction.objects.get_or_create(
            comment=comment, user=request.user
        )
        if reaction.is_dislike:
            reaction.delete()
            return Response({"details": "Dislike has been removed"}, status=status.HTTP_200_OK)
        else:
            reaction.is_dislike = True
            reaction.save()
            return Response({"details": "Dislike has been added"}, status=status.HTTP_200_OK)
