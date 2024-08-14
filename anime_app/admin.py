from django.contrib import admin

from anime_app.models import CharacterModel, AnimeModel, MangaModel

# Register your models here.

admin.site.register(AnimeModel)
admin.site.register(CharacterModel)
admin.site.register(MangaModel)
