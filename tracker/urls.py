from tracker.views import HabitViewSet
from django.urls import path

urlpatterns = [
    path('habits/', HabitViewSet.as_view())
]