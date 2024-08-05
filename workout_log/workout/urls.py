from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('workouts', views.WorkoutViewSet)
router.register('exercises', views.ExerciseViewSet)
router.register('weighttypes', views.WeightTypeViewSet)
router.register('sets', views.SetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
