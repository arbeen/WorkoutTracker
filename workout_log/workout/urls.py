from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('workouts', views.WorkoutViewSet)
router.register('exercises', views.ExerciseViewSet)
router.register('weighttypes', views.WeightTypeViewSet)
router.register('sets', views.SetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recommend/', views.recommend_view, name='recommend'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('test/', views.Test.as_view(), name='test'),
]
