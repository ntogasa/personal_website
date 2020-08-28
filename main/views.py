from django.shortcuts import render
from django.views import generic


def home_view(request):
    """Handles requests for the 'home' page"""
    return render(request, 'home.html')


def about_view(request):
    """Handles requests for the 'about me' page"""
    return render(request, 'about.html')


def photography_view(request):
    """Handles requests for the 'photography' page"""
    return render(request, 'photography.html')


def side_projects_view(request):
    """Handles requests for the 'photography' page"""
    return render(request, 'side_projects.html')


def writing_view(request):
    """Handles requests for the 'writing' page"""
    return render(request, 'writing.html')