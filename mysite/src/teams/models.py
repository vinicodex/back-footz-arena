from django.db import models
from src.tournament.models import Tournament


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name