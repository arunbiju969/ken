# Generated by Django 5.1.7 on 2025-03-12 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournamentpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamregistration',
            name='team_logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/team_logos/{team_name}/'),
        ),
    ]
