from django.urls import path
from . import views

urlpatterns = [
    path("", views.scrims_list, name="scrims_list"),
    path("<int:scrim_id>/", views.scrim_detail, name="scrim_detail"),
    path("leaderboard/", views.scrims_leaderboard, name="scrims_leaderboard"),
]
