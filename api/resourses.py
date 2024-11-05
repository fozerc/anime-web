from itertools import chain

from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from anime_app.models import AnimeModel, CharacterModel, MangaModel
from api.serializers import AnimeSerializer, AnimeCharacterSerializer, MangaSerializer


class AnimeModelViewSet(viewsets.ModelViewSet):
    serializer_class = AnimeSerializer
    queryset = AnimeModel.objects.all()
    permission_classes = []


class CharacterModelViewSet(viewsets.ModelViewSet):
    serializer_class = AnimeCharacterSerializer
    queryset = CharacterModel.objects.all()
    permission_classes = []


class MangaModelViewSet(viewsets.ModelViewSet):
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
        print('aaaaa')
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
