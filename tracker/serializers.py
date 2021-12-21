from rest_framework import serializers
from tracker.models import Counter, Habit


class HabitPostSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = ['name', 'owner']




class HabitSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = ['name', 'created_at', 'count', 'owner']

    @staticmethod
    def get_count(obj):
        return Counter.objects.filter(habit_id=obj.id).count()


