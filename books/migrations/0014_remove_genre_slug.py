# Generated by Django 3.1.7 on 2021-03-07 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_genre_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='slug',
        ),
    ]
