from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    registration_deadline = models.DateTimeField()
    image_url = models.URLField(max_length=200)
    event_url = models.URLField(max_length=200)
    event_rules = models.TextField()

    def __str__(self):
        return self.title
