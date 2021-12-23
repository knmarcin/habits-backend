from tracker.views import HabitViewSet, HabitDetailView, AddCountView
from django.urls import path

urlpatterns = [
    path('habits', HabitViewSet.as_view()),
    path('habits/<int:pk>', HabitDetailView.as_view()),
    path('count/<int:pk>', AddCountView.as_view()),
]
