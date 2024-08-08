from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)

from .views import calculate_one_rep_max

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('workouts', views.WorkoutViewSet)
router.register('exercises', views.ExerciseViewSet)
router.register('weighttypes', views.WeightTypeViewSet)
router.register('sets', views.SetViewSet)
router.register("userprofile", views.UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),
    path('recommend/', views.recommend_view, name='recommend'),
    path('one_rep_max/', calculate_one_rep_max, name='calculate_one_rep_max'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('test/', views.Test.as_view(), name='test'),
]
