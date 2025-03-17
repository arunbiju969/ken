from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from Events.models import EventType, Game, EventDetails


class Command(BaseCommand):
    help = "Populate the database with dummy data for EventDetails"

    def handle(self, *args, **kwargs):
        # Create Event Types
        event_type1 = EventType.objects.create(name="Tournament")
        event_type2 = EventType.objects.create(name="Scrim")

        # Create Games
        game1 = Game.objects.create(name="Valorant", game_id="valorant", platform="PC")
        game2 = Game.objects.create(
            name="League of Legends", game_id="lol", platform="PC"
        )

        # Create Event Details
        EventDetails.objects.create(
            title="Valorant Championship",
            event_type=event_type1,
            description="A competitive Valorant tournament.",
            date=timezone.now() + datetime.timedelta(days=30),
            location="New York",
            game=game1,
            registration_deadline=timezone.now() + datetime.timedelta(days=20),
            image_url=None,
            event_external_url="https://example.com/valorant-championship",
            stream_url="https://twitch.tv/valorant",
            stream_type="Twitch",
            event_rules="Standard Valorant rules apply.",
            status="upcoming",
            teams=16,
        )

        EventDetails.objects.create(
            title="League of Legends Scrim",
            event_type=event_type2,
            description="A friendly scrim for League of Legends teams.",
            date=timezone.now() + datetime.timedelta(days=15),
            location="Los Angeles",
            game=game2,
            registration_deadline=timezone.now() + datetime.timedelta(days=10),
            image_url=None,
            event_external_url="https://example.com/lol-scrim",
            stream_url="https://youtube.com/lol-scrim",
            stream_type="YouTube",
            event_rules="Standard League of Legends rules apply.",
            status="ongoing",
            teams=8,
        )

        self.stdout.write(self.style.SUCCESS("Dummy data created successfully."))
