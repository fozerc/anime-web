from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class AnimeUser(AbstractUser):
    name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    email = models.EmailField()


class CharacterModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class AnimeModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    characters = models.ForeignKey(CharacterModel, on_delete=models.CASCADE)
    year_of_issue = models.DateField(blank=True, null=True)

    def str_(self):
        return self.name


class MangaModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    characters = models.ForeignKey(CharacterModel, on_delete=models.CASCADE)
    year_of_issue = models.DateField(blank=True, null=True)

    def str_(self):
        return self.name


class PostModel(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey('SectionModel', on_delete=models.CASCADE)
    description = models.TextField()


class SectionModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='section_images/')
    title = models.CharField(max_length=100)
    user = models.ForeignKey(AnimeUser, on_delete=models.CASCADE)


class WikiModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    theme = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    sections = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    community_posts = models.ForeignKey(PostModel, on_delete=models.CASCADE, blank=True, null=True)


class Comment(models.Model):
    user = models.ForeignKey(AnimeUser, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def likes_count(self):
        return self.reactions.filter(is_liked=True).count()

    def dislikes_count(self):
        return self.reactions.filter(is_liked=False).count()


class CommentReaction(models.Model):
    user = models.ForeignKey(AnimeUser, on_delete=models.CASCADE, related_name='comment_reactions')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reactions')
    is_like = models.BooleanField(blank=True, null=True)
    is_dislike = models.BooleanField(blank=True, null=True)

    class Meta:
        unique_together = (('user', 'comment'),)
