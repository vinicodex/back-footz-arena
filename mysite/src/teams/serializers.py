from rest_framework import serializers
from .models import Team

class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    instagram = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    isCaptain = serializers.BooleanField()

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'tournament', 'players']

    def create(self, validated_data):
        players_data = validated_data.pop('players')
        team = Team.objects.create(**validated_data)
        for player_data in players_data:
            team.players.create(**player_data)
        return team
