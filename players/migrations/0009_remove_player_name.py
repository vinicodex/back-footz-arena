# Generated by Django 5.0.6 on 2024-05-13 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_player_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
    ]
