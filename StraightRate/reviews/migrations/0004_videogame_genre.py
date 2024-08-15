# Generated by Django 5.0.7 on 2024-08-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_movie_poster_videogame_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='genre',
            field=models.CharField(choices=[('Action-Adventure', 'Action-Adventure'), ('RPG', 'Role-Playing Game'), ('FPS', 'First Person Shooter'), ('MMO', 'MMO'), ('Strategy', 'Strategy'), ('Sports', 'Sports'), ('Horror', 'Horror'), ('Fighting', 'Fighting'), ('Racing', 'Racing'), ('Platformer', 'Platformer'), ('Survival', 'Survival')], default='Action', max_length=100, verbose_name='Genre'),
            preserve_default=False,
        ),
    ]