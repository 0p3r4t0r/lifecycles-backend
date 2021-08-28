from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Goal(models.Model):
    range = 100

    name = models.CharField(max_length=255, unique=True)
    points = models.IntegerField(validators=[
        MaxValueValidator(range),
        MinValueValidator(-range),
    ])


class Daily(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.DO_NOTHING)
    done = models.BooleanField(null=True)
    default = models.BooleanField()
    date = models.DateField()