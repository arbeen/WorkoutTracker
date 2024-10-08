import time
from decimal import Decimal

from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, status, serializers
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from openai import OpenAI
from .serializers import UserSerializer, WorkoutSerializer, ExerciseSerializer, WeightTypeSerializer, SetSerializer, \
    RecommendSerializer, OneRepMaxSerializer, UserWorkoutSerializer, UserProfileSerializer, UserSetSerializer
from .models import Workout, Exercise, WeightType, Set


class Test(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


def get_chatgpt_response(data):
    client = OpenAI()
    thread = client.beta.threads.create(
        messages=[
            {
                'role': 'user',
                'content': f'Recommend a weight loss plan for someone who currently weighs {data['current_weight']} kg, wants to reach {data['goal_weight']} kg in {data['duration']}.'
            }
        ]
    )
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=settings.ASSISTANT_KEY)
    print(run.id)

    while run.status != 'completed':
        time.sleep(3)

    message_res = client.beta.threads.messages.list(thread_id=thread.id)
    latest_mess = message_res.data[0]  # get the latest reply
    answer = latest_mess.content[0].text.value

    return answer


@api_view(['POST'])
# @permission_classes([permissions.AllowAny])
def recommend_view(request):
    serializer = RecommendSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        # content = {'message': 'Hehe!'}
        # return Response(content)
        chatgpt_response = get_chatgpt_response(data)
        return Response({'recommendation': chatgpt_response}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# The 1RM is calculated using the Epley formula: 1RM = weight + (weight * reps * 0.0333).
@api_view(['POST'])
def calculate_one_rep_max(request):
    serializer = OneRepMaxSerializer(data=request.data)
    if serializer.is_valid():
        exercise_id = serializer.validated_data['exercise_id']
        sets = Set.objects.filter(exercise_id=exercise_id).order_by('-weight')
        if sets:
            max_set = sets[0]
            one_rep_max = max_set.weight + (max_set.weight * max_set.reps * Decimal('0.0333'))
            return Response({'one_rep_max': one_rep_max}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No sets found for this exercise'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ViewSet):
    def list(self, request):
        user = User.objects.get(username=request.user.username)
        workouts = Workout.objects.filter(user=user)
        sets = Set.objects.filter(workout__in=workouts)

        user_serializer = UserProfileSerializer(user)
        workout_serializer = UserWorkoutSerializer(workouts, many=True)
        set_serializer = UserSetSerializer(sets, many=True)

        return Response({
            'user': user_serializer.data,
            'workouts': workout_serializer.data,
            'sets': set_serializer.data,
        })


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
