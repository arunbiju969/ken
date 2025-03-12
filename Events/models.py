from django.db import models

class EventType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    id = models.CharField(max_length=50, primary_key=True)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('tournament', 'Tournament'),
        ('scrims', 'Scrims'),
        ('watchparty', 'Watchparty'),
        ('giveaway', 'Giveaway'),
    ]

    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    registration_deadline = models.DateTimeField()
    image_url = models.URLField(max_length=200)
    event_url = models.URLField(max_length=200)
    event_rules = models.TextField()

    def __str__(self):
        return self.title
