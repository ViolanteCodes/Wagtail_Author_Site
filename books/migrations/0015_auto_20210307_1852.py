# Generated by Django 3.1.7 on 2021-03-07 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_remove_genre_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentwarning',
            old_name='warning_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contentwarning',
            name='warning_slug',
        ),
    ]
