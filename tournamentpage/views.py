from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeamRegistrationForm
from .models import TeamRegistration
from Events.models import EventDetails
from .utils import (
    get_filter_options,
    calculate_tournament_bracket,
)  # Import the utility function


def tournament_detail(request, tournament_id):
    # Fetch the specific tournament from the database
    tournament = get_object_or_404(EventDetails, id=tournament_id)

    # Mock data for teams
    teams = [{"name": f"Team {i + 1}", "id": i + 1} for i in range(tournament.teams)]

    # Add some sample scores for demonstration (first round matches)
    if tournament.teams >= 4:
        teams[0]["score"] = 2
        teams[1]["score"] = 1
        teams[2]["score"] = 0
        teams[3]["score"] = 2

    # Calculate bracket structure
    bracket_data = calculate_tournament_bracket(tournament.teams, teams)

    context = {"tournament": tournament, "teams": teams, "bracket_data": bracket_data}

    return render(request, "tournamentpage/tournament_detail.html", context)


def tournament_list(request):
    # Get filter parameters from the request
    selected_game = request.GET.get("game")
    selected_platform = request.GET.get("platform")
    selected_status = request.GET.get("status")

    # Fetch all tournaments from the EventDetails model
    tournaments = EventDetails.objects.filter(event_type__name="Tournament")

    # Apply filters
    filters_applied = False
    if selected_game:
        tournaments = tournaments.filter(game__name=selected_game)
        filters_applied = True
    if selected_platform:
        tournaments = tournaments.filter(game__platform=selected_platform)
        filters_applied = True
    if selected_status:
        tournaments = tournaments.filter(status=selected_status.lower())
        filters_applied = True

    # Fetch featured tournaments from the EventDetails model
    featured_tournaments = tournaments.filter(status="upcoming")[:2]

    # Get filter options
    filter_options = get_filter_options()

    # Define breadcrumb items
    if filters_applied:
        breadcrumb_items = [
            {"name": "Home", "url": "index"},
            {"name": "Tournaments", "url": "tournament_list"},
            {"name": "Filtered Tournaments", "url": None},
        ]
    else:
        breadcrumb_items = [
            {"name": "Home", "url": "index"},
            {"name": "Tournaments", "url": "tournament_list"},
            {"name": "Featured Tournaments", "url": None},
        ]

    context = {
        "featured_tournaments": featured_tournaments,
        "tournaments": tournaments,
        "selected_game": selected_game,
        "selected_platform": selected_platform,
        "selected_status": selected_status,
        "filters_applied": filters_applied,
        "breadcrumb_items": breadcrumb_items,
        **filter_options,  # Include filter options in the context
    }

    return render(request, "tournamentpage/tournament.html", context)


def register_team(request):
    if request.method == "POST":
        form = TeamRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "registration_success"
            )  # Update to your desired success URL name
    else:
        form = TeamRegistrationForm()
    return render(request, "partials/_team_registration.html", {"form": form})


def registered_teams(request):
    teams = TeamRegistration.objects.all()  # Optionally filter by tournament if needed
    return render(request, "tournamentpage/registered_teams.html", {"teams": teams})


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
    if filters_applied:
        breadcrumb_items = [
            {"name": "Home", "url": "index"},
            {"name": "Scrims", "url": "scrims_list"},
            {"name": "Filtered Scrims", "url": None},
        ]
    else:
        breadcrumb_items = [
            {"name": "Home", "url": "index"},
            {"name": "Scrims", "url": "scrims_list"},
            {"name": "Featured Scrims", "url": None},
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

    return render(request, "tournamentpage/scrims.html", context)


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
        request, "tournamentpage/scrims_leaderboard.html", {"leaderboard": leaderboard}
    )
