from fitness.api.exercise import ExerciesViewSet
from fitness.apps import FitnessConfig
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'exercises', ExerciesViewSet)

app_name = FitnessConfig.name
urlpatterns = [
    path('', include(router.urls)),
]