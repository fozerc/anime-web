from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.resources import AnimeModelViewSet, CharacterModelViewSet, MangaModelViewSet, GlobalSearchListAPIView, \
    AnimeUserRegistration, LogoutAPIView, WikiModelViewSet, PostModelViewSet, SectionModelViewSet

router = routers.DefaultRouter()
router.register(r'anime', AnimeModelViewSet, basename='anime')
router.register(r'character', CharacterModelViewSet, basename='anime-character')
router.register(r'manga', MangaModelViewSet, basename='anime-manga')
router.register(r'wiki', WikiModelViewSet, basename='wiki')
router.register(r'post', PostModelViewSet, basename='post')
router.register(r'section', SectionModelViewSet, basename='section')

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth_token'),
    path('global-search/', GlobalSearchListAPIView.as_view(), name='global-search'),
    path("register/", AnimeUserRegistration.as_view(), name="register"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
