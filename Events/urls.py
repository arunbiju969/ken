from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_view, name="index"),
    path("<int:event_id>/", views.event_detail, name="event_detail"),
]
