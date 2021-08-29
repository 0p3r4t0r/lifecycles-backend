from goals.models import OverInterval
from rest_framework import serializers
from rest_framework import viewsets, permissions


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OverInterval
        fields = ['name', 'points', 'times', 'days']


class Viewset(viewsets.ModelViewSet):
    serializer_class = Serializer
    permission_classes =[ permissions.IsAuthenticated ]
    queryset = OverInterval.objects.all().order_by('name')

