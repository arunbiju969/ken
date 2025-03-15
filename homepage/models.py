# filepath: c:\Users\arunb\Documents\Project\Django\KEN\ken\homepage\models.py
from django.db import models


class Slide(models.Model):
    image = models.ImageField(upload_to="slides/")
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.platform


class SiteSettings(models.Model):
    qr_data = models.URLField()
    instagram_reel_permalink = models.URLField()

    def __str__(self):
        return "Site Settings"
