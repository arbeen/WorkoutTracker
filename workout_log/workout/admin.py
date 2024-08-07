from django.contrib import admin
from .models import Set, Workout, Exercise, WeightType
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('workout', 'exercise', 'reps', 'weight', 'weight_type', 'rest_time', 'is_warmup', 'created_at', 'updated_at')
    list_filter = ('workout', 'exercise', 'is_warmup')
    search_fields = ('workout', 'exercise', 'is_warmup')
    ordering = ('workout', 'exercise', 'is_warmup')
    
@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'date', 'description', 'created_at', 'updated_at')
    list_filter = ('user', 'date')
    search_fields = ('user', 'date')
    ordering = ('user', 'date')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_predefined', 'created_at', 'updated_at')
    list_filter = ('is_predefined',)
    search_fields = ('name', 'is_predefined')
    ordering = ('name', 'is_predefined')
    
@admin.register(WeightType)
class WeightTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
