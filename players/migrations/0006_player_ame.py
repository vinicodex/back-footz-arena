# Generated by Django 4.0.4 on 2024-05-12 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_remove_player_user_player_birth_date_player_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='ame',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
