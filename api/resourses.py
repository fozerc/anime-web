from rest_framework import viewsets

from anime_app.models import AnimeModel
from api.serializers import AnimeSerializer


class AnimeModelViewSet(viewsets.ModelViewSet):
    serializer_class = AnimeSerializer
    queryset = AnimeModel.objects.all()
    permission_classes = []


class