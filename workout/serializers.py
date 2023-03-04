from rest_framework import serializers
from .models import Workout, Exercise


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    """serializingo all exercises"""
    class Meta:
        model = Exercise
        fields = '__all__'


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    """serializeng all exercises"""
    class Meta:
        model = Workout
        fields = '__all__'


