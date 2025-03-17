from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeamRegistrationForm
from .models import TeamRegistration
from Events.models import EventDetails, Game  # Import the EventDetails and Game models
from .utils import get_filter_options  # Import the utility function
import math


def calculate_tournament_bracket(team_count, teams_data=None):
    """
    Calculate tournament bracket structure based on number of teams.
    Returns a complete data structure for the template to render.
    """
    # Default team data if not provided
    if teams_data is None:
        teams_data = [{"name": f"Team {i + 1}", "id": i + 1} for i in range(team_count)]

    # Calculate total rounds needed
    rounds_count = math.ceil(math.log2(team_count))

    # Calculate byes needed
    next_power_of_two = 2**rounds_count
    byes_count = next_power_of_two - team_count
    has_byes = byes_count > 0

    # Generate bracket structure
    bracket = []

    # First round setup with proper seeding
    first_round_matches = []

    # For 5 teams, we should have 2 matches (4 teams) + 1 bye (1 team)
    # The number of matches in round 1 is floor(team_count/2)
    match_count = team_count // 2

    # Create the matches
    for i in range(match_count):
        first_round_matches.append(
            {
                "is_bye": False,
                "team1": teams_data[i * 2],
                "team2": teams_data[i * 2 + 1],
                "winner": None,  # No winner yet
                "round": 1,
                "match_number": i + 1,
            }
        )

    # Add byes for remaining teams
    # For 5 teams, only team5 gets a bye
    for i in range(match_count * 2, team_count):
        first_round_matches.append(
            {
                "is_bye": True,
                "team1": teams_data[i],
                "team2": None,
                "winner": teams_data[i],  # Team with bye automatically advances
                "round": 1,
                "match_number": match_count + (i - match_count * 2) + 1,
            }
        )

    bracket.append(
        {
            "round_number": 1,
            "round_name": "Round 1",
            "matches": first_round_matches,
            "spacing": 8,  # Base spacing
        }
    )

    # Generate subsequent rounds
    remaining_teams = team_count - byes_count  # For round 1 (actual matches)

    for r in range(2, rounds_count + 1):
        # Calculate teams advancing from previous round
        previous_matches = bracket[r - 2]["matches"]
        remaining_teams = len(previous_matches)  # Winners from previous round

        matches_in_round = remaining_teams // 2
        byes_in_round = remaining_teams % 2
        round_matches = []

        # Calculate visual spacing for this round
        spacing = 8 * (2 ** (r - 1))

        # Create regular matches
        for i in range(matches_in_round):
            round_matches.append(
                {
                    "is_bye": False,
                    "team1": None,
                    "team2": None,
                    "winner": None,
                    "round": r,
                    "match_number": i + 1,
                }
            )

        # Add byes if needed
        for i in range(byes_in_round):
            round_matches.append(
                {
                    "is_bye": True,
                    "team1": None,
                    "team2": None,
                    "winner": None,
                    "round": r,
                    "match_number": matches_in_round + i + 1,
                }
            )

        round_name = (
            "Finals"
            if r == rounds_count
            else "Semifinals"
            if r == rounds_count - 1
            else f"Round {r}"
        )

        bracket.append(
            {
                "round_number": r,
                "round_name": round_name,
                "matches": round_matches,
                "spacing": spacing,
            }
        )

    return {
        "bracket": bracket,
        "rounds_count": rounds_count,
        "team_count": team_count,
        "has_byes": has_byes,
        "byes_count": byes_count,
    }


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
    tournaments = EventDetails.objects.all()

    # Apply filters
    if selected_game:
        tournaments = tournaments.filter(game__name=selected_game)
    if selected_platform:
        tournaments = tournaments.filter(game__platform=selected_platform)
    if selected_status:
        tournaments = tournaments.filter(status=selected_status.lower())

    # Fetch featured tournaments from the EventDetails model
    featured_tournaments = tournaments.filter(status="upcoming")[:2]

    # Get filter options
    filter_options = get_filter_options()

    context = {
        "featured_tournaments": featured_tournaments,
        "tournaments": tournaments,
        "selected_game": selected_game,
        "selected_platform": selected_platform,
        "selected_status": selected_status,
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


def scrims_page(request):
    # Get filter options
    filter_options = get_filter_options()

    context = {
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
