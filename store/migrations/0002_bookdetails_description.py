# Generated by Django 5.0.4 on 2024-05-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookdetails",
            name="description",
            field=models.CharField(blank=True, default="", max_length=250, null=True),
        ),
    ]
