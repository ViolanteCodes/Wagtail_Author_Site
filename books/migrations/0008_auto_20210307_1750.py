# Generated by Django 3.1.7 on 2021-03-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210307_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentwarning',
            old_name='slug',
            new_name='warning_slug',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='slug',
            new_name='genre_slug',
        ),
    ]
