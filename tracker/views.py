import datetime

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError

from tracker.models import Habit, Counter
from tracker.serializers import HabitSerializer, HabitPostSerializer, CounterSerializer


class HabitViewSet(APIView):
    @staticmethod
    def get(request):
        try:
            queryset = Habit.objects.filter(owner_id=request.user)
            serializer = HabitSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TypeError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def post(request):
        """Creates Habit"""
        serializer = HabitPostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            name = serializer.validated_data['name']
            new_object = Habit.objects.create(name=name, owner=request.user)
            new_object.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabitDetailView(APIView):

    @staticmethod
    def get(request, pk):
        obj = Habit.objects.get(pk=pk)
        serializer = HabitSerializer(obj)
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        obj = Habit.objects.get(pk=pk)
        serializer = HabitPostSerializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        obj = Habit.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddCountView(APIView):
    """
    first post requests create counter obj,
    second post removes it
    """

    @staticmethod
    def post(request, pk):
        try:
            serializer = CounterSerializer(data=request.data)
            if serializer.is_valid():
                Counter.objects.create(habit_id=pk)
                return Response(serializer.data)
        except IntegrityError:
            obj = Counter.objects.get(accomplished=datetime.date.today(), habit_id=pk)
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors)
