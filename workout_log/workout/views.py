from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, status, serializers
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, WorkoutSerializer, ExerciseSerializer, WeightTypeSerializer, SetSerializer
from .models import Workout, Exercise, WeightType, Set


class Test(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def logout(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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
