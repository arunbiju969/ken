from django.contrib import admin
from .models import EventDetails, EventType, Game

admin.site.register(EventDetails)
admin.site.register(EventType)
admin.site.register(Game)
