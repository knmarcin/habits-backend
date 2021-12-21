from django.db import models


class Habit(models.Model):
    '''Simple model for Habit, soon to be added FK to user.'''
    name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)


class Counter(models.Model):
    '''Simple counters for habits with unique date/habit_id'''
    accomplished = models.DateField(auto_now_add=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('accomplished', 'habit',)
