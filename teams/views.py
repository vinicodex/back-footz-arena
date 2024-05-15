from django.shortcuts import render
from tournament.models import Rule, Tournament
from teams.models import Team
from players.models import Player


def index(request):
    return render(request, 'index.html')


def read_rules(request):
    rules = Rule.objects.all()
    return render(request, 'rules.html', context={'rules': rules})


def subscribe(request):
    if request.method == 'GET':
        return render(request, 'subscribe.html')

    if request.method == 'POST':
        data = request.POST.dict()
        team_filter = Team.objects.filter(name__icontains=data['team_name']).first()
        if not team_filter:
            tournament = Tournament.objects.all()[0]
            team_filter = Team.objects.create(name=data['team_name'], tournament=tournament)

        if Player.objects.filter(first_name__icontains=data['captain_name'], instagram_user__icontains=data['captain_instagram']).exists():
            error = {'error': f'Já existe um capitão com esse nome {data["captain_name"]} e {data["captain_instagram"]}.'}
            return render(request, 'subscribe.html', context=error)

        players = [data['player_1_name'], data['player_2_name'], data['player_3_name']]

        if Player.objects.filter(first_name__in=players).exists():
            error = {'Já existe um jogador com esse nome cadastrado'}
            return render(request, 'subscribe.html', context=error)


        Player.objects.create(first_name=data['captain_name'],
                              phone_number=data['captain_phone'],
                              instagram_user=data['captain_instagram'],
                              is_captain=True,
                              team=team_filter)
        Player.objects.create(first_name=data['player_1_name'],
                              instagram_user=data['player_1_instagram'],
                              team=team_filter)
        Player.objects.create(first_name=data['player_2_name'],
                              instagram_user=data['player_2_instagram'],
                              team=team_filter)
        Player.objects.create(first_name=data['player_3_name'],
                              instagram_user=data['player_3_instagram'],
                              team=team_filter)
        return render(request, 'index.html')
