# Generated by Django 3.2.8 on 2021-11-03 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 15, 58, 15, 181267)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 15, 58, 15, 181267)),
        ),
    ]
