# Generated by Django 4.1.1 on 2022-09-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="Email Address"
            ),
        ),
    ]