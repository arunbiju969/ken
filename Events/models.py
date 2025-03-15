from django.db import models


class EventType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EventDetails(models.Model):
    title = models.CharField(max_length=200)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    game = models.CharField(max_length=200, null=True, blank=True, default="Valorant")
    registration_deadline = models.DateTimeField()
    image_url = models.ImageField(
        upload_to="event_images/", blank=True, null=True, help_text="Optional"
    )
    event_external_url = models.URLField(
        max_length=200, blank=True, null=True, help_text="Optional"
    )
    stream_url = models.URLField(
        max_length=200, blank=True, null=True, help_text="Optional"
    )
    stream_type = models.CharField(
        max_length=200, blank=True, null=True, help_text="Optional"
    )
    event_rules = models.TextField(blank=True, null=True, help_text="Optional")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Event Detail"
        verbose_name_plural = "Event Details"
