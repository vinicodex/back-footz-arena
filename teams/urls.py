from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.team_list_create.as_view(), name='team-list-create'),
]
