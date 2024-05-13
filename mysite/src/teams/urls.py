from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamListCreate.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', views.TeamRetrieveUpdateDestroy.as_view(), name='team-detail'),
]
