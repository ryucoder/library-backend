# Generated by Django 4.2 on 2024-12-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="avg_rating",
            field=models.FloatField(default=0.0),
        ),
    ]
