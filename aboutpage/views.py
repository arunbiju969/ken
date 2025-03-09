from django.shortcuts import render


def about(request):
    return render(request, "aboutpage/about.html")
