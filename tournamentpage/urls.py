from django.urls import path
from . import views

urlpatterns = [
    path("", views.tournament_list, name="tournament_list"),
    path("<int:tournament_id>/", views.tournament_detail, name="tournament_detail"),
    path("register/", views.register_team, name="register_team"),
    path("registered-teams/", views.registered_teams, name="registered_teams"),
    path("scrims/", views.scrims_list, name="scrims_list"),
    path("scrims/leaderboard/", views.scrims_leaderboard, name="scrims_leaderboard"),
]
