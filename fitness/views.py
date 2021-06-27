
from rest_framework import viewsets, permissions

from .models import Exercise
from .serializers import ExerciseSerializer


class ExerciesViewSet(viewsets.ModelViewSet):
    """
    API end point to get exercises.
    """
    serializer_class = ExerciseSerializer
    permission_classes = [ permissions.IsAuthenticated ]
    queryset = Exercise.objects.all().order_by('name')