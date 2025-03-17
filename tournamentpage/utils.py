from Events.models import Game


def get_filter_options():
    games = Game.objects.values_list("name", flat=True).distinct()
    platforms = Game.objects.values_list("platform", flat=True).distinct()
    statuses = ["Upcoming", "Ongoing", "Completed"]

    return {
        "games": games,
        "platforms": platforms,
        "statuses": statuses,
    }
