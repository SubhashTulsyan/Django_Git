# Generated by Django 3.2.8 on 2021-11-03 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_student_created_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 39, 31, 63492)),
        ),
    ]
