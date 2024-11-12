from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.resourses import AnimeModelViewSet, CharacterModelViewSet, MangaModelViewSet, GlobalSearchListAPIView, \
    RegisterCreateAPIView

router = routers.DefaultRouter()
router.register(r'anime', AnimeModelViewSet, basename='anime')
router.register(r'character', CharacterModelViewSet, basename='anime-character')
router.register(r'manga', MangaModelViewSet, basename='anime-manga')

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth_token'),
    path('global-search', GlobalSearchListAPIView.as_view(), name='global-search'),
    path('register', csrf_exempt(RegisterCreateAPIView.as_view()), name='register'),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
