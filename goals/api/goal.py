from goals.models import Goal
from rest_framework import serializers
from rest_framework import viewsets, permissions


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ['name', 'points']


class Viewset(viewsets.ModelViewSet):
    serializer_class = Serializer
    permission_classes =[ permissions.IsAuthenticated ]
    queryset = Goal.objects.all().order_by('name')

