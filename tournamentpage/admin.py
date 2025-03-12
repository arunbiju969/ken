from django.contrib import admin
from .models import TeamRegistration


@admin.register(TeamRegistration)
class TeamRegistrationAdmin(admin.ModelAdmin):
    list_display = ["team_name", "registrant_email", "created_at"]
    search_fields = ["team_name", "registrant_email"]
    list_filter = ["created_at"]
