from rest_framework.test import APITestCase
from .models import Exercise, Workout


class TestViews(APITestCase):
    url = "/workouts/workouts/1/"
    data = {'url': 'http://testserver/workouts/workouts/1/', 'title': 'treningA'}

    def setUp(self):
        Workout.objects.create(title="treningA")

    def test_get_exercise(self):
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result, self.data)