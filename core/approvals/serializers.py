from rest_framework import serializers
from .models import Approval


class ApprovalSerializer(serializers.ModelSerializer):
    approved_by_username = serializers.CharField(source='approved_by.username', read_only=True)

    class Meta:
        model = Approval
        fields = [
            'id', 'operation', 'approved_by', 'approved_by_username',
            'decision', 'comment', 'timestamp'
        ]
        read_only_fields = ['timestamp']