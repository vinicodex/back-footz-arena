from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Player, Tournament
from .serializers import TeamSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def team_list_create(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        tournament = get_object_or_404(Tournament, pk=1)

        team_name = request.data.get('teamName')
        if Team.objects.filter(name=team_name).exists():
            return Response({'error': 'Team already exists'}, status=status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(name=team_name)

        players_data = request.data.get('players', [])
        for player_data in players_data:
            Player.objects.create(
                first_name=player_data.get('name'),
                birth_date=player_data.get('dob'),
                email=player_data.get('email'),
                phone_number=player_data.get('phone'),
                instagram_user=player_data.get('instagram'),
                team=team,
                is_captain=player_data.get('is_captain', False),
            )

        team.tournament = tournament
        team.save()
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
