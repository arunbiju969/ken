from django.shortcuts import render
from datetime import datetime, timedelta
from django.utils import timezone
from Events.models import Event

def index(request):
    # Define dynamic slides for the carousel
    slides = [
        {"image": "img/1.png", "alt": "Slide 1"},
        {"image": "img/2.png", "alt": "Slide 2"},
    ]

    # Sample latest news data
    latest_news = []

    # Sample upcoming events data
    current_date = datetime.now()

    events = Event.objects.all().order_by('date')

    context = {"slides": slides, "latest_news": latest_news, "events": events}
    return render(request, "homepage/index.html", context)


def sandbox(request):
    return render(request, "homepage/sandbox.html")
