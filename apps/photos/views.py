from django.shortcuts import render

# Create your views here.
def photo_gallery_view(request):
    return render(request, 'photos/photography.html')