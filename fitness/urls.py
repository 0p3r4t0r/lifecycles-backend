from django.urls import include, path
from rest_framework import routers, urlpatterns
from .apps import FitnessConfig
from . import views


router = routers.DefaultRouter()
router.register(r'exercises', views.ExerciesViewSet)

app_name = FitnessConfig.name
urlpatterns = [
    path('', include(router.urls)),
]