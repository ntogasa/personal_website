from django.shortcuts import render
from .models import Photo


# Create your views here.
def photo_gallery_view(request):
    photos = Photo.objects.filter(status=1)
    context = {
        'photos': photos,
    }
    return render(request, 'photos/gallery.html', context)