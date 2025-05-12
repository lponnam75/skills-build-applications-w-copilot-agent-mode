from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password')
        activity = Activity.objects.create(user=user, activity_type='Running', duration='01:00:00')
        self.assertEqual(activity.activity_type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Description')
        self.assertEqual(workout.name, 'Test Workout')

    def test_workout_description(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Description')
        self.assertEqual(workout.description, 'Test Description')

    def test_workout_str(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Description')
        self.assertEqual(str(workout), 'Test Workout')

    def test_workout_duration(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password')
        activity = Activity.objects.create(user=user, activity_type='Running', duration='01:00:00')
        workout = Workout.objects.create(name='Test Workout', description='Test Description', activity=activity)
        self.assertEqual(workout.activity.duration, '01:00:00')

    def test_workout_leaderboard_integration(self):
        user = User.objects.create(username='testuser', email='test@example.com', password='password')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        workout = Workout.objects.create(name='Test Workout', description='Test Description')
        workout.leaderboard.add(leaderboard)
        self.assertIn(leaderboard, workout.leaderboard.all())