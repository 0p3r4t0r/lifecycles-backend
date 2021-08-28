
from fitness.models import Exercise
from rest_framework import serializers
from rest_framework import viewsets, permissions


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name']


class ExerciesViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    permission_classes = [ permissions.IsAuthenticated ]
    queryset = Exercise.objects.all().order_by('name')

