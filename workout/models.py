from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Workout(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100, blank=True, default="trening")
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'

class Exercise(models.Model):
    bodyparts = (
        ('shoulders', 'Shoulders'),
        ('arms', 'Arms'),
        ('legs', 'Legs'),
        ('back', 'Back'),
        ('chest', 'Chest')
        )
    objects = models.Manager()
    title = models.CharField(max_length=100)
    series = models.IntegerField(default=1)
    reps = models.IntegerField(default=1)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    bodypart = models.CharField(max_length=20, default='other', choices=bodyparts)
    def __str__(self) -> str:
        return f'{self.title}'


