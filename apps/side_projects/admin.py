from django.contrib import admin
from .models import SideProject

# Register your models here.

class SideProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'status')
    list_filter = ('status',)

# Register your models here
admin.site.register(SideProject, SideProjectsAdmin)