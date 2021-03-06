# Generated by Django 3.2.8 on 2021-10-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='a', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, help_text='HelpEmail', max_length=254),
        ),
    ]
