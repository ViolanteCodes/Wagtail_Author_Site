# Generated by Django 3.1.7 on 2021-03-09 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210309_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='repeat_in_subnav',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='repeated_item_text',
        ),
    ]