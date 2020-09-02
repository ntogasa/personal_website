from django.contrib import admin
from .models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('alt', 'date_uploaded', 'status')
    list_filter = ('status',)

# Register your models here.
admin.site.register(Photo, PhotoAdmin)