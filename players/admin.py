from django.contrib import admin
from src.players.models import Player

admin.site.register(Player)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'gender', 'birth_date')
