from django.shortcuts import render
from django.views import generic


def home_view(request):
    """Handles requests for the homepage"""
    return render(request, 'home.html')
