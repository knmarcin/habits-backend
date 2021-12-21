from rest_framework import serializers
from tracker.models import Counter, Habit


class HabitSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = ['name','habit', 'count']

    def get_count(self, obj):
        return Habit.objects.filter(id=obj.habit.id).count()
