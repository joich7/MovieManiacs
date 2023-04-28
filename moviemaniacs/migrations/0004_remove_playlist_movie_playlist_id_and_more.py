# Generated by Django 4.2 on 2023-04-27 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviemaniacs', '0003_playlist_movie_movie_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist_movie',
            name='playlist_id',
        ),
        migrations.AddField(
            model_name='playlist_movie',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='moviemaniacs.playlist'),
        ),
    ]
