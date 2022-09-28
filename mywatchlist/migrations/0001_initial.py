# Generated by Django 4.1 on 2022-09-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('release_date', models.CharField(max_length=255)),
                ('review', models.TextField()),
            ],
        ),
    ]
