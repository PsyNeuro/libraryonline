# Generated by Django 5.0.4 on 2024-06-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_bookdetails_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookdetails",
            name="genre",
            field=models.CharField(default="None", max_length=50),
        ),
    ]
