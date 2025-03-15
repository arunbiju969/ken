def get_filter_options():
    games = ["All Games", "Valorant"]
    platforms = ["All Platforms", "PC"]
    statuses = ["All Status", "Upcoming", "Ongoing", "Completed"]

    return {
        "games": games,
        "platforms": platforms,
        "statuses": statuses,
    }
