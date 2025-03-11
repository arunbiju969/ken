from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", include("aboutpage.urls")),  # About page URLs
    path("tournament/", include("tournamentpage.urls")),  # Tournament page URLs
    path("events/", include("Events.urls")),  # Events URLs
    path("", include("homepage.urls")),  # Home page URLs (catch-all)
]
