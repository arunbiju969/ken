from django.shortcuts import render, get_object_or_404
from Events.models import EventDetails
from tournamentpage.forms import TeamRegistrationForm  # If needed for registration
from tournamentpage.utils import get_filter_options


def scrim_detail(request, scrim_id):
    # Fetch the specific scrim from the database
    scrim = get_object_or_404(EventDetails, id=scrim_id)

    # Mock data for teams
    teams = [{"name": f"Team {i + 1}", "id": i + 1} for i in range(scrim.teams)]

    context = {"scrim": scrim, "teams": teams}

    return render(request, "scrimpage/scrim_detail.html", context)


def scrims_list(request):
    # Get filter parameters from the request
    selected_game = request.GET.get("game")
    selected_platform = request.GET.get("platform")
    selected_status = request.GET.get("status")

    # Fetch all scrims from the EventDetails model
    scrims = EventDetails.objects.filter(event_type__name="Scrim")

    # Apply filters
    filters_applied = False
    if selected_game:
        scrims = scrims.filter(game__name=selected_game)
        filters_applied = True
    if selected_platform:
        scrims = scrims.filter(game__platform=selected_platform)
        filters_applied = True
    if selected_status:
        scrims = scrims.filter(status=selected_status.lower())
        filters_applied = True

    # Fetch featured scrims from the EventDetails model
    featured_scrims = scrims.filter(status="upcoming")[:2]

    # Get filter options
    filter_options = get_filter_options()

    # Define breadcrumb items
    breadcrumb_items = [
        {"name": "Home", "url": "index"},
        {"name": "Scrims", "url": "scrims_list"},
    ]

    context = {
        "featured_scrims": featured_scrims,
        "scrims": scrims,
        "selected_game": selected_game,
        "selected_platform": selected_platform,
        "selected_status": selected_status,
        "filters_applied": filters_applied,
        "breadcrumb_items": breadcrumb_items,
        **filter_options,  # Include filter options in the context
    }

    return render(request, "scrimpage/scrims.html", context)


def scrims_leaderboard(request):
    leaderboard = [
        {
            "name": "Team Phoenix",
            "wins": 12,
            "losses": 3,
            "points": 100,
            "logo": "images/phoenix.png",
        },
        {
            "name": "Shadow Hunters",
            "wins": 10,
            "losses": 5,
            "points": 30,
            "logo": "images/shadow.png",
        },
        {
            "name": "Cyber Warriors",
            "wins": 9,
            "losses": 6,
            "points": 50,
            "logo": "images/cyber.png",
        },
        {
            "name": "Nightmare Squad",
            "wins": 8,
            "losses": 7,
            "points": 24,
            "logo": "images/nightmare.png",
        },
        {
            "name": "Thunderbolts",
            "wins": 7,
            "losses": 8,
            "points": 40,
            "logo": "images/thunder.png",
        },
    ]

    # Sort by points (descending) and then by wins (if points are tied)
    leaderboard = sorted(leaderboard, key=lambda x: (-x["points"], -x["wins"]))

    return render(
        request, "scrimpage/scrims_leaderboard.html", {"leaderboard": leaderboard}
    )
