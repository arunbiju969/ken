from django.shortcuts import render, get_object_or_404
from .models import EventDetails


def event_detail(request, event_id):
    event = get_object_or_404(EventDetails, id=event_id)
    return render(request, "Events/event_detail.html", {"event": event})
