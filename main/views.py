from django.shortcuts import render
from django.apps import apps


def home_view(request):
    """Handles requests for the 'home' page"""
    writing_pieces = apps.get_model('writing', 'WritingPieces')
    featured_pieces = writing_pieces.objects.filter(feature=1).order_by('-date')
    context = {'featured_pieces': featured_pieces[:3]}
    return render(request, 'home.html', context)


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