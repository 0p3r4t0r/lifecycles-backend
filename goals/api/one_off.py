from goals.models import OneOff
from rest_framework import serializers
from rest_framework import viewsets, permissions


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OneOff
        fields = ['name', 'points']


class Viewset(viewsets.ModelViewSet):
    serializer_class = Serializer
    permission_classes =[ permissions.IsAuthenticated ]
    queryset = OneOff.objects.all().order_by('name')

