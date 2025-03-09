# filepath: /c:/Users/arunb/Documents/Project/Django/KEN/homepage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
