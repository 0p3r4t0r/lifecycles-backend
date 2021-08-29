from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from accounts.models import User
from lifeCycles.models import TimeStampMixin


class Goal(models.Model):
    class Meta:
        abstract = True

    range = 100

    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    points = models.IntegerField(validators=[
        MaxValueValidator(range),
        MinValueValidator(-range),
    ])


class OneOff(Goal, TimeStampMixin):
    """Achieve once"""
    completed_at = models.DateTimeField(blank=True, null=True)


class OverInterval(Goal, TimeStampMixin):
    """Achieve n times over a period of t time."""
    class Interval(models.IntegerChoices):
        DAILY = 1
        WEEKLY = 7 

    count_to_complete = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    interval_in_days = models.IntegerField(choices=Interval.choices)


class OverIntervalCompletion(models.Model):
    """Track the completion times of  goals."""
    over_interval = models.ForeignKey(OverInterval, on_delete=models.CASCADE)
    completed_at = models.DateTimeField()