from django.urls import path
from . import views

urlpatterns = [
    path("", views.tournament_list, name="tournament_list"),
    path("<int:tournament_id>/", views.tournament_detail, name="tournament_detail"),
    path("register/", views.register_team, name="register_team"),
    path("registered-teams/", views.registered_teams, name="registered_teams"),
]
