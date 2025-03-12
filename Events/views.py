from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Event
from django.utils import timezone

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'Events/event_detail.html', {'event': event})

def upcoming_events(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'partials/_upcoming_events.html', {'events': events,"page_title": "Upcoming Gaming Events",})
    
def my_view(request):
    # Generate sample event data
    current_date = datetime.now()

    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')

    context = {
        "events": events,
        "page_title": "Upcoming Gaming Events",
    }

    return render(request, "Events/my_template.html", context)

