from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Event
from django.utils import timezone

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'Events/event_detail.html', {'event': event})