# Generated by Django 3.2.8 on 2021-11-09 14:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('content', models.TextField(max_length=1000)),
                ('createdBy', models.OneToOneField(limit_choices_to={'is_staff': False}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('date', models.DateField(default=datetime.date(2021, 11, 9))),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('postId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.post')),
                ('likes', models.IntegerField()),
            ],
            bases=('app1.post',),
        ),
    ]