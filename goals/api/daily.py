from goals.models import Daily
from rest_framework import serializers
from rest_framework import viewsets, permissions


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Daily
        fields = ['goal', 'done']


class Viewset(viewsets.ModelViewSet):
    serializer_class = Serializer
    permission_classes =[ permissions.IsAuthenticated ]
    queryset = Daily.objects.all().order_by('goal.name')

