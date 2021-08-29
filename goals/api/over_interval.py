from goals.models import OverInterval
from rest_framework import serializers
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OverInterval
        fields = ['name', 'points', 'count_to_complete', 'interval_in_days']

    def create(self, validated_data):
        validated_data['user_id'] = self._context['request'].user.id
        return super().create(validated_data)


class Viewset(viewsets.ModelViewSet):
    serializer_class = Serializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = OverInterval.objects.all().order_by('created_at')

    def list(self, request):
        queryset = (OverInterval.objects
            .filter(user_id=request.user.id)
            .order_by('created_at'))
        serializer = Serializer(queryset, many=True)
        return Response(serializer.data)
