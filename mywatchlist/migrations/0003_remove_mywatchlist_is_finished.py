# Generated by Django 4.1 on 2022-09-28 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_mywatchlist_is_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mywatchlist',
            name='is_finished',
        ),
    ]
