from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response

from tracker.models import Habit, Counter
from tracker.serializers import HabitSerializer, HabitPostSerializer

class HabitViewSet(APIView):
    def get(self, request):
        try:
            queryset = Habit.objects.filter(owner_id=request.user)
            serializer = HabitSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except (TypeError):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    def post(self, request):
        serializer = HabitPostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            name = serializer.validated_data['name']

            new_object = Habit.objects.create(name=name, owner=request.user)
            new_object.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
