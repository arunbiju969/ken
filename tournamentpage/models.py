from django.db import models
import os

def team_logo_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/static/team_logos/<team_name>/<filename>
    return os.path.join('static', 'team_logos', instance.team_name, filename)

class TeamRegistration(models.Model):
    team_name = models.CharField(max_length=100)
    team_logo = models.ImageField(
        upload_to=team_logo_upload_path, blank=True, null=True
    )

    # Required players (1 to 5)
    player1 = models.CharField(max_length=50)
    player1_riot_id = models.CharField(max_length=50)

    player2 = models.CharField(max_length=50)
    player2_riot_id = models.CharField(max_length=50)

    player3 = models.CharField(max_length=50)
    player3_riot_id = models.CharField(max_length=50)

    player4 = models.CharField(max_length=50)
    player4_riot_id = models.CharField(max_length=50)

    player5 = models.CharField(max_length=50)
    player5_riot_id = models.CharField(max_length=50)

    # Optional players (6 and 7)
    player6 = models.CharField(max_length=50, blank=True, null=True)
    player6_riot_id = models.CharField(max_length=50, blank=True, null=True)

    player7 = models.CharField(max_length=50, blank=True, null=True)
    player7_riot_id = models.CharField(max_length=50, blank=True, null=True)

    registrant_email = models.EmailField(help_text="Your email address")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name
