# Generated by Django 5.2 on 2025-04-30 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_favoritegame'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoritegame',
            old_name='game_title',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='favoritegame',
            old_name='comment',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='favoritegame',
            old_name='platform',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='favoritegame',
            old_name='gamer_name',
            new_name='title',
        ),
    ]
