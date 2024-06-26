from django.contrib import admin

from players.models import Player
from teams.models import Team



class PlayersInline(admin.TabularInline):
    model = Player
    readonly_fields = ['id', 'first_name', 'instagram_user']
    fields = ['id', 'first_name', 'instagram_user']

class TeamAdmin(admin.ModelAdmin):

    list_display = ['name']

    inlines = (PlayersInline,)

admin.site.register(Team, TeamAdmin)
