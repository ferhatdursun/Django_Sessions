# Generated by Django 4.1.1 on 2022-09-29 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='path',
            old_name='path',
            new_name='path_name',
        ),
    ]
