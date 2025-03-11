from django.shortcuts import render, redirect
from .forms import TeamRegistrationForm
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
    # In a real app, you'd fetch the specific tournament from database
    tournament = {
        "id": tournament_id,
        "name": "Kerala Esports Championship 2025"
        if tournament_id == 1
        else f"Tournament {tournament_id}",
        "image": "img/ft_tour.png",
        "game": "Valorant",
        "game_icon": "img/val_icon.png",
        "prize": "1,00,000",
        "date": "Mar 15-20, 2025",
        "location": "Kochi",
        "teams": 6,  # Changed to 7 for testing odd number
        "format": "5v5 Double Elimination",
        "description": "The flagship esports tournament bringing together the best teams across Kerala to compete for glory!",
        "rules": [
            "5v5 team format",
            "Double elimination bracket",
            "Best of 3 matches",
            "Standard competitive rules apply",
        ],
        "status": "Upcoming",
        "champion": None,  # No champion yet
    }

    # Mock data for teams
    teams = [{"name": f"Team {i + 1}", "id": i + 1} for i in range(tournament["teams"])]

    # Add some sample scores for demonstration (first round matches)
    if tournament["teams"] >= 4:
        teams[0]["score"] = 2
        teams[1]["score"] = 1
        teams[2]["score"] = 0
        teams[3]["score"] = 2

    # Calculate bracket structure
    bracket_data = calculate_tournament_bracket(tournament["teams"], teams)

    context = {"tournament": tournament, "teams": teams, "bracket_data": bracket_data}

    return render(request, "tournamentpage/tournament_detail.html", context)


def tournament_list(request):
    # Featured tournaments
    featured_tournaments = [
        {
            "id": 1,
            "name": "Kerala Esports Championship 2025",
            "image": "img/ft_tour.png",
            "game": "Valorant",
            "game_icon": "img/val_icon.png",
            "prize": "1,00,000",
            "date": "Mar 15-20, 2025",
            "location": "Kochi",
            "teams": 8,
            "description": "The flagship esports tournament bringing together the best teams across Kerala to compete for glory!",
            "status": "Upcoming",
        },
        {
            "id": 2,
            "name": "Kerala Mobile Gaming Fest",
            "image": "img/mobile_gaming_fest.png",
            "game": "PUBG Mobile",
            "game_icon": "img/pubg_icon.png",
            "prize": "50,000",
            "date": "Apr 10-12, 2025",
            "location": "Thiruvananthapuram",
            "teams": 16,
            "description": "A thrilling mobile gaming tournament featuring the best PUBG Mobile teams.",
            "status": "Upcoming",
        },
    ]

    # Tournament list
    tournaments = [
        # Add sample tournaments
    ]

    # Filter options
    games = [
        "All Games",
        "Valorant",
    ]
    platforms = [
        "All Platforms",
        "PC",
    ]
    statuses = ["All Status", "Upcoming", "Ongoing", "Completed"]

    context = {
        "featured_tournaments": featured_tournaments,
        "tournaments": tournaments,
        "games": games,
        "platforms": platforms,
        "statuses": statuses,
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
