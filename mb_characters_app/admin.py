from django.contrib import admin

from mb_characters_app.models import AnimeUser, CharacterModel, MangaModel, PostModel, SectionModel, WikiModel

admin.site.register(AnimeUser)
admin.site.register(CharacterModel)
admin.site.register(MangaModel)
admin.site.register(PostModel)
admin.site.register(SectionModel)
admin.site.register(WikiModel)
