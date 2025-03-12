from django.urls import path
from . import views

urlpatterns = [
    path('upcoming-events/', views.upcoming_events, name='upcoming_events'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    # other paths...
]
