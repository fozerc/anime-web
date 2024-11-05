from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class AnimeUser(AbstractUser):
    name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatars/')
    email = models.EmailField(unique=True, )

    groups = models.ManyToManyField(
        Group,
        related_name="animeuser_groups",
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="animeuser_permissions",
        blank=True,
        help_text="Specific permissions for this user."
    )


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
