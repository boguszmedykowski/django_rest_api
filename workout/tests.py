from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Workout, Exercise
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status


class TestWorkout(APITestCase):

    def setUp(self):
        Workout.objects.create(title="treningA")


    def test_get_workout(self):
        # url = reverse('')
        response = self.client.get('/workout/workouts/1/', format='json')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content[0]['title'], 'treningA')

    def test_post_workout(self):
        response = self.client.post("/workout/workouts/", data={'title': 'treningE'})
        self.assertEqual(response.status_code, 201)
        # self.assertEqual(response.content, b'{"url":"http://testserver/workout/workouts/2/","title":"treningE"}')

class TestCreateWorkout(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test_user1', password='12345678')
        Workout.objects.create(title='traning')
        workout = Workout.objects.get(pk=1)
        Exercise.objects.create(title='tescik', workout=workout)

    def test_workout_content(self):
        workout = Workout.objects.get(pk=1)
        title = f"{workout.title}"
        self.assertEqual(title, 'traning')
        self.assertEqual(str(workout), 'traning')

    def test_exercise_content(self):
        exercise = Exercise.objects.get(pk=1)
        title = f"{exercise.title}"
        self.assertEqual(title, 'tescik')
        self.assertEqual(str(exercise), 'tescik')

    def test_user(self):
        user = User.objects.get(pk=1)
        username = f"{user.username}"
        self.assertEqual(username, 'test_user1')



