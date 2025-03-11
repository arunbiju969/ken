import qrcode
import base64
from io import BytesIO
from django.shortcuts import render


def index(request):
    # Define dynamic slides for the carousel
    slides = [
        {"image": "img/1.png", "alt": "Slide 1"},
        {"image": "img/2.png", "alt": "Slide 2"},
    ]

    context = {"slides": slides}
    return render(request, "homepage/index.html", context)


def sandbox(request):
    return render(request, "homepage/sandbox.html")
