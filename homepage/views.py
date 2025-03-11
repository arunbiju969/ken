from django.shortcuts import render


def index(request):
    # Define dynamic slides for the carousel
    slides = [
        {"image": "img/1.png", "alt": "Slide 1"},
        {"image": "img/2.png", "alt": "Slide 2"},
    ]

    # Sample latest news data
    latest_news = []

    # Sample upcoming events data
    events = [
        {
            "id": 1,
            "title": "Kerala Gaming Championship",
            "description": "The biggest gaming tournament in Kerala featuring competitions in Valorant, CS:GO, and FIFA 23.",
            "image_url": "https://example.com/path/to/image1.jpg",
        },
        {
            "id": 2,
            "title": "Esports Workshop & Networking",
            "description": "Learn from professional esports players and connect with teams and sponsors in this exclusive networking event.",
            "image_url": "https://example.com/path/to/image2.jpg",
        },
        {
            "id": 3,
            "title": "Mobile Gaming Festival",
            "description": "A day dedicated to mobile gaming featuring PUBG Mobile, Call of Duty Mobile, and Clash Royale tournaments with cash prizes.",
            "image_url": "https://example.com/path/to/image3.jpg",
        },
    ]

    context = {"slides": slides, "latest_news": latest_news, "events": events}
    return render(request, "homepage/index.html", context)


def sandbox(request):
    return render(request, "homepage/sandbox.html")
