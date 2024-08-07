import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)  # workout name , maybe not compulsory for now ??
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Exercise List Inventory
class Exercise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)  # Ensure unique exercise names
    description = models.TextField(blank=True, null=True)
    is_predefined = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WeightType(models.Model):
    name = models.CharField(max_length=10, choices=[('kg', 'Kilograms'), ('lb', 'Pounds')])


# Each individual exercise set performed in a workout
class Set(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workout = models.ForeignKey(Workout,
                                on_delete=models.CASCADE)  # each set is part of a workout , you may do 315lb bench press as a part of monday workout
    exercise = models.ForeignKey(Exercise,
                                 on_delete=models.CASCADE)  # which exercise ? maybe id of bench press Exercise
    reps = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # number of repetitions done in that set
    weight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])  # weight used
    weight_type = models.ForeignKey(WeightType, on_delete=models.CASCADE, null=True, blank=True)  # Optional
    rest_time = models.PositiveIntegerField(default=0)
    is_warmup = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
