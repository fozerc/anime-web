# Generated by Django 5.0.7 on 2024-08-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_app', '0003_mangamodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactermodel',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='charactermodel',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='charactermodel',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
