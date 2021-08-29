from goals.models import OverInterval
from rest_framework import serializers
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OverInterval
        fields = ['name', 'points', 'count_to_complete', 'interval_in_days']


class Viewset(viewsets.ModelViewSet):
    serializer_class = Serializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = OverInterval.objects.all()

    def get_queryset(self):
        user = self.request.user
        return OverInterval.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user_id=user.id)
