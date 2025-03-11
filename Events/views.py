from django.shortcuts import render
from datetime import datetime, timedelta


def my_view(request):
    # Generate sample event data
    current_date = datetime.now()

    events = [
        {
            "id": 1,
            "title": "Kerala Gaming Championship",
            "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
            "date": (current_date + timedelta(days=7)).strftime("%B %d, %Y"),
            "description": "The biggest gaming tournament in Kerala featuring competitions in Valorant, CS:GO, and FIFA 23.",
            "location": "Cochin International Convention Center",
            "registration_deadline": (current_date + timedelta(days=3)).strftime(
                "%B %d, %Y"
            ),
        },
        {
            "id": 2,
            "title": "Esports Workshop & Networking",
            "image_url": "https://images.unsplash.com/photo-1551436712-4710c8e3d918?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
            "date": (current_date + timedelta(days=14)).strftime("%B %d, %Y"),
            "description": "Learn from professional esports players and connect with teams and sponsors in this exclusive networking event.",
            "location": "Trivandrum Tech Hub",
            "registration_deadline": (current_date + timedelta(days=10)).strftime(
                "%B %d, %Y"
            ),
        },
        {
            "id": 3,
            "title": "Mobile Gaming Festival",
            "image_url": "https://images.unsplash.com/photo-1560253023-3ec5d502959f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
            "date": (current_date + timedelta(days=21)).strftime("%B %d, %Y"),
            "description": "A day dedicated to mobile gaming featuring PUBG Mobile, Call of Duty Mobile, and Clash Royale tournaments with cash prizes.",
            "location": "Lulu Mall, Kochi",
            "registration_deadline": (current_date + timedelta(days=17)).strftime(
                "%B %d, %Y"
            ),
        },
        {
            "id": 4,
            "title": "Game Development Hackathon",
            "image_url": "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
            "date": (current_date + timedelta(days=30)).strftime("%B %d, %Y"),
            "description": "48-hour hackathon for game developers to create innovative games based on Kerala's culture and heritage.",
            "location": "Kerala Startup Mission, Kochi",
            "registration_deadline": (current_date + timedelta(days=25)).strftime(
                "%B %d, %Y"
            ),
        },
        {
            "id": 5,
            "title": "Virtual Reality Experience Day",
            "image_url": "https://images.unsplash.com/photo-1622979135225-d2ba269cf1ac?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
            "date": (current_date + timedelta(days=45)).strftime("%B %d, %Y"),
            "description": "Try out the latest VR gaming technology and participate in VR gaming competitions.",
            "location": "Infopark, Kochi",
            "registration_deadline": (current_date + timedelta(days=40)).strftime(
                "%B %d, %Y"
            ),
        },
        {
            "id": 6,
            "title": "College Esports League Finals",
            "image_url": "https://images.unsplash.com/photo-1605806616949-1e87b487fc2f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
            "date": (current_date + timedelta(days=60)).strftime("%B %d, %Y"),
            "description": "The culmination of the inter-college esports league featuring the top college teams from across Kerala.",
            "location": "NIT Calicut",
            "registration_deadline": "Closed",
        },
    ]

    context = {
        "events": events,
        "page_title": "Upcoming Gaming Events",
    }

    return render(request, "Events/my_template.html", context)


def event_detail(request, event_id):
    # In a real app, you'd get the event from the database
    # For now, we'll generate sample data like in my_view
    current_date = datetime.now()

    # Sample events (same as in my_view)
    events = [
        {
            "id": 1,
            "title": "Kerala Gaming Championship",
            "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80",
            "date": (current_date + timedelta(days=7)).strftime("%B %d, %Y"),
            "description": "The biggest gaming tournament in Kerala featuring competitions in Valorant, CS:GO, and FIFA 23.",
            "location": "Cochin International Convention Center",
            "registration_deadline": (current_date + timedelta(days=3)).strftime(
                "%B %d, %Y"
            ),
        },
        # Include all your other events here
    ]

    # Find the requested event
    event = next((e for e in events if e["id"] == event_id), None)

    if not event:
        # Handle case where event doesn't exist
        from django.http import Http404

        raise Http404("Event not found")

    context = {"event": event, "page_title": event["title"]}

    return render(request, "Events/event_detail.html", context)
