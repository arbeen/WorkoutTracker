from rest_framework import viewsets
from .serializers import UserSerializer, WorkoutSerializer, ExerciseSerializer, WeightTypeSerializer, SetSerializer
from .models import User, Workout, Exercise, WeightType, Set


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WeightTypeViewSet(viewsets.ModelViewSet):
    queryset = WeightType.objects.all()
    serializer_class = WeightTypeSerializer


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
