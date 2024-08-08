from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User, Workout, Exercise, WeightType, Set


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data["password"])
        return user


class RecommendSerializer(serializers.Serializer):
    current_weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    goal_weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    duration = serializers.CharField(max_length=100)

class OneRepMaxSerializer(serializers.Serializer):
    exercise_id = serializers.UUIDField()

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WeightTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightType
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'
