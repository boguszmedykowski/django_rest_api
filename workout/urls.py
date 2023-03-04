from rest_framework import routers
from .views import ExerciseViewSet, WorkoutViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'workouts', WorkoutViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]