from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    '''Simple model for Habit, soon to be added FK to user.'''
    name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Counter(models.Model):
    '''Simple counters for habits with unique date/habit_id'''
    accomplished = models.DateField(auto_now_add=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('accomplished', 'habit',)
