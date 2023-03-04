from .serializers import ExerciseSerializer, WorkoutSerializer
from .models import Exercise, Workout
from rest_framework import viewsets


class ExerciseViewSet(viewsets.ModelViewSet):

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutViewSet(viewsets.ModelViewSet):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
