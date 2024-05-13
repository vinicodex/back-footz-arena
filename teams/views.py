from rest_framework import generics, status
from rest_framework.response import Response
from .models import Team
from django.contrib.auth.models import User
from .serializers import TeamSerializer
from tournament.models import Tournament
from ..players.models import Player


class TeamListCreate(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        tournament = Tournament.objects.get(pk=1)

        if Team.objects.filter(name=request.data['teamName']).first():
            return Response({'error': 'Team already exists'}, status=status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(name=request.data['teamName'])

        for player in request.data['players']:
            Player.objects.create(
                first_name=player.get('name', None),
                birth_date=player.get('dob', None),
                email=player.get('email', None),
                phone_number=player.get('phone', None),
                instagram_user=player.get('instagram', None),
                team=team,
                is_captain=player.get('is_captain', None),
            )
        team.tournament = tournament
        team.save()
        return Response(status=status.HTTP_201_CREATED)



class TeamRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
