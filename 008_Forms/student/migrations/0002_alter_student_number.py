# Generated by Django 4.1.1 on 2022-09-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="number",
            field=models.IntegerField(null=True),
        ),
    ]
