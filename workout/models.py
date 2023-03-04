from django.db import models




class Exercise(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    series = models.IntegerField(default=1)
    reps = models.IntegerField(default=1)
    def __str__(self) -> str:
        return f'{self.title}'


class Workout(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100, blank=True, default="trening")
    # date = models.DateField(auto_now_add=True , blank=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.title}'