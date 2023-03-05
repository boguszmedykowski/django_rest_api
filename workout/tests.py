from rest_framework.test import APITestCase
from .models import Workout

class Testcase(APITestCase):

    def setUp(self):
        Workout.objects.create(title="treningA")


    def test_get_workout(self):
        response = self.client.get('/workout/workouts/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_workout(self):
        response = self.client.post("/workout/workouts/", data={'title': 'treningE'})
        self.assertEqual(response.status_code, 201)
        # self.assertEqual(response.content, b'{"url":"http://testserver/workout/workouts/2/","title":"treningE"}')










# class TestViews(APITestCase):
#     url = "/workouts/workouts/1/"

#     def setUp(self):
#         Workout.objects.create(title="treningA")

#     def test_get_workout(self):
#         response = self.client.get(self.url)
#         result = response.json()

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(result["title"], "treningA")

#     def test_post_workout(self):

#         data = {
#             "title": "treningB"
#         }
#         factory = APIRequestFactory()
#         request = factory.post(self.url, data, format='json')

