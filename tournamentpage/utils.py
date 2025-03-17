from Events.models import Game
import math


def get_filter_options():
    games = Game.objects.values_list("name", flat=True).distinct()
    platforms = Game.objects.values_list("platform", flat=True).distinct()
    statuses = ["Upcoming", "Ongoing", "Completed"]

    return {
        "games": games,
        "platforms": platforms,
        "statuses": statuses,
    }


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
