# Generated by Django 4.1.1 on 2022-09-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("relations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
