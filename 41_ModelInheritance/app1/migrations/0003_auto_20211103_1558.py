# Generated by Django 3.2.8 on 2021-11-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20211103_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='date',
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(),
        ),
    ]
