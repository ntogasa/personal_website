from django.shortcuts import render
from .models import WritingPieces

# Create your views here.
def writing_view(request):
    writing_pieces = WritingPieces.objects.filter(status=1).order_by('-date_published')
    context = {'writing_pieces': writing_pieces}
    return render(request, 'writing/writing.html', context)
