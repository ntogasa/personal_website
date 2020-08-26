from django.shortcuts import render
from django.views import generic


def home_view(request):
    """Handles requests for the homepage"""
    return render(request, 'home.html')


def about_view(request):
    """Accepts a request and returns the rendered 'about.html' template."""
    return render(request, 'about.html')


