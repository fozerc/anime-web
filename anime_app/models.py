from django.db import models


class CharacterModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')


class AnimeModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    characters = models.ForeignKey(CharacterModel, on_delete=models.CASCADE)
    year_of_issue = models.DateField()
