# Generated by Django 4.2.1 on 2023-05-06 03:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hackathon", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hackathon",
            name="participants",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                related_name="participating_hackathons",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]