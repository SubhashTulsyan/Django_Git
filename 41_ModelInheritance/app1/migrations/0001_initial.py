# Generated by Django 3.2.8 on 2021-11-03 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 11, 3, 15, 57, 58, 195280))),
                ('roll', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 11, 3, 15, 57, 58, 195280))),
                ('emp_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]