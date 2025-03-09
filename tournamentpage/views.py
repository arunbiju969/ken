from django.shortcuts import render


def tournament(request):
    # Sample data with stages and their corresponding matches
    stages = [
        {
            "name": "Group Stage",
            "matches": [
                {"teams": "Team A vs Team B", "date": "2025-03-10", "time": "10:00 AM"},
                {"teams": "Team C vs Team D", "date": "2025-03-10", "time": "12:00 PM"},
            ],
        },
        {
            "name": "Quarter Finals",
            "matches": [
                {"teams": "Team E vs Team F", "date": "2025-03-11", "time": "03:00 PM"},
                {"teams": "Team G vs Team H", "date": "2025-03-11", "time": "05:00 PM"},
            ],
        },
        {
            "name": "Semi Finals",
            "matches": [
                {
                    "teams": "Winner QF1 vs Winner QF2",
                    "date": "2025-03-12",
                    "time": "06:00 PM",
                },
            ],
        },
        {
            "name": "Final",
            "matches": [
                {
                    "teams": "Winner SF vs Winner SF",
                    "date": "2025-03-13",
                    "time": "08:00 PM",
                },
            ],
        },
    ]
    context = {"stages": stages}
    return render(request, "tournamentpage/tournament.html", context)
