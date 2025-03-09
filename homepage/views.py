# filepath: /c:/Users/arunb/Documents/Project/Django/KEN/homepage/views.py
from django.shortcuts import render


def index(request):
    return render(request, "homepage/index.html")
