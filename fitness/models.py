from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    seconds_on = models.IntegerField(help_text="Time working out.")
    seconds_off = models.IntegerField(help_text="Time resting between sets.") 


class Workout(models.Model):
    sets = models.ManyToManyField(Set, verbose_name="list of sets", through='Routine')


class Routine(models.Model):
    ordinal = models.IntegerField()
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

