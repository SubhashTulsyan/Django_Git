# Generated by Django 3.2.8 on 2021-11-03 16:40

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_student_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('students', django.db.models.manager.Manager()),
            ],
        ),
    ]