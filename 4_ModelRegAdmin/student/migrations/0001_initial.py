# Generated by Django 3.2.8 on 2021-10-24 06:50

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
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(choices=[('-1', '--Select--'), ('CS', 'Computer Science'), ('ME', 'Mechanical Engineering')], default='-1', max_length=100)),
            ],
        ),
    ]
