from django.shortcuts import render
from .models import SideProject

# Create your views here.
def side_projects_view(request):
    side_projects = SideProject.objects.filter(status=1)
    context = {'side_projects': side_projects}
    return render(request, 'side_projects/side_projects.html', context)
