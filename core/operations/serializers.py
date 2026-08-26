from rest_framework import serializers
from .models import Operation


class OperationSerializer(serializers.ModelSerializer):
    requested_by_username = serializers.CharField(source='requested_by.username', read_only=True)
    device_name = serializers.CharField(source='device.name', read_only=True)

    class Meta:
        model = Operation
        fields = [
            'id', 'device', 'device_name', 'command', 'operation_type',
            'status', 'requested_by', 'requested_by_username',
            'created_at', 'executed_at'
        ]
        read_only_fields = ['status', 'created_at', 'executed_at']