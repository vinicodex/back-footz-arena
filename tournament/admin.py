from django.contrib import admin
from tournament.models import Tournament, Rule


class RulesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_3v3')

admin.site.register(Rule, RulesAdmin)
admin.site.register(Tournament)
