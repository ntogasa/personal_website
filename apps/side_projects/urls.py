from django.urls import path
from . import views

urlpatterns = [
    path('', views.side_projects_view, name='side_projects'),
    ]