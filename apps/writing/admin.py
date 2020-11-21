from django.contrib import admin
from .models import WritingPieces

# Register your models here.

class WritingPiecesAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_link', 'date', 'publication', 'syndication','feature', 'status')
    list_filter = ('status',)

# Register your models here
admin.site.register(WritingPieces, WritingPiecesAdmin)