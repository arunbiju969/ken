# Generated by Django 5.1.7 on 2025-03-12 19:19

import tournamentpage.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournamentpage", "0002_alter_teamregistration_team_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teamregistration",
            name="team_logo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=tournamentpage.models.team_logo_upload_path,
            ),
        ),
    ]
