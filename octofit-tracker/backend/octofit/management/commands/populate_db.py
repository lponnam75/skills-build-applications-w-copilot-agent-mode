from django.core.management.base import BaseCommand
from octofit.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta
from django.apps import apps
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Populate users
        for user_data in test_users:
            User.objects.create(**user_data)

        # Populate teams
        for team_data in test_teams:
            members = team_data.pop('members')
            team = Team.objects.create(**team_data)
            team.members.set(User.objects.filter(username__in=members))

        # Populate activities
        for activity_data in test_activities:
            user = User.objects.get(username=activity_data.pop('user'))
            Activity.objects.create(user=user, **activity_data)

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            user = User.objects.get(username=leaderboard_data.pop('user'))
            Leaderboard.objects.create(user=user, **leaderboard_data)

        # Populate workouts
        for workout_data in test_workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
