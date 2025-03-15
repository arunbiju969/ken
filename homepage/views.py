from django.shortcuts import render
from Events.models import EventDetails
from .models import Slide


def index(request):
    # Fetch slides from the database
    slides = Slide.objects.all()

    # Sample latest news data
    latest_news = []

    events = EventDetails.objects.all().order_by("date")

    context = {"slides": slides, "latest_news": latest_news, "events": events}
    return render(request, "homepage/index.html", context)


def sandbox(request):
    return render(request, "homepage/sandbox.html")
