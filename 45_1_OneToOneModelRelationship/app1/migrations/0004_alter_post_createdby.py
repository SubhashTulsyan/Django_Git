# Generated by Django 3.2.8 on 2021-11-09 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0003_auto_20211109_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdBy',
            field=models.OneToOneField(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]