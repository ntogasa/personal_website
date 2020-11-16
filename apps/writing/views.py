from django.shortcuts import render
from .models import WritingPieces

# Create your views here.
def writing_view(request):
    writing_pieces = WritingPieces.objects.filter(status=1).order_by('-date')
    featured_pieces = WritingPieces.objects.filter(feature=1).order_by('-date')
    context = {'writing_pieces': writing_pieces,
               'featured_pieces': featured_pieces[:2]}
    return render(request, 'writing/writing.html', context)
