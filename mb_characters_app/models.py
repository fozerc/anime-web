from django.contrib.auth.models import AbstractUser
from django.db import models


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


"""
сделать в след раз модели и полностью продумать логику того как будет работать идея с вики и постами в сообществе
прописать вообще все модели и их поля, выделить для этого отдельный день чтобы я смогу всё нормально продумать и т.д 
след главной задачей прописать поля для вики с постами и т.д не забыть о том что я ещё хотел грузхить несколько картинок 
сразу, основная идея заключается в том чтобы я создал вики с постами и сообществами в которых каждый может создавать
 своё типо амино но лучше.
"""


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
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

"""
начать реализовывать лайки к коментам с след раз и посмотреть в чате
"""
