from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from api.resourses import AnimeModelViewSet, CharacterModelViewSet, MangaModelViewSet, GlobalSearchListAPIView, \
    RegisterCreateAPIView

router = routers.DefaultRouter()
router.register(r'anime', AnimeModelViewSet, basename='anime')
router.register(r'character', CharacterModelViewSet, basename='anime-character')
router.register(r'manga', MangaModelViewSet, basename='anime-manga')


urlpatterns = [
    path('', include(router.urls)),
    path('global-search', GlobalSearchListAPIView.as_view(), name='global-search'),
    path('register', RegisterCreateAPIView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
