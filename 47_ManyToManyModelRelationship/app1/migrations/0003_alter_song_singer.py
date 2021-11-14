# Generated by Django 3.2.8 on 2021-11-09 16:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_alter_song_singer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
