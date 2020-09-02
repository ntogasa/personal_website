from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_gallery_view, name='photography'),
    ]