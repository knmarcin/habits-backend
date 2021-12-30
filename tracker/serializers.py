from rest_framework import serializers
from tracker.models import Counter, Habit
from django.contrib.auth.models import User


class HabitPostSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Habit
        fields = ['name', 'owner']


class HabitSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()


    class Meta:
        model = Habit
        fields = ['name', 'created_at', 'count', 'owner', 'id']

    @staticmethod
    def get_count(obj):
        return Counter.objects.filter(habit_id=obj.id).count()


class CounterSerializer(serializers.ModelSerializer):
    accomplished = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Counter
        fields = ('habit', 'accomplished')

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(min_length=2)
    password = serializers.CharField(min_length=6, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')