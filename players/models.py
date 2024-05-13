from django.contrib.auth.models import User
from django.db import models
from src.teams.models import Team


class Player(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    instagram_user = models.CharField(max_length=50,blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_captain = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.instagram_user}"
