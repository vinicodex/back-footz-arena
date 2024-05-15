from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.team_list_create, name='team-list-create'),
]
