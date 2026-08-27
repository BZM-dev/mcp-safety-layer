from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Operation
from .serializers import OperationSerializer
from audit.models import AuditLog 


def log_action(user, action, operation, details=""):
    AuditLog.objects.create(
        user=user,
        action=action,
        related_operation=operation,
        details=details,
    )

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Operation.objects.all()
        return Operation.objects.filter(requested_by=user)

    def perform_create(self, serializer):
        operation = serializer.save(requested_by=self.request.user, status='pending')
        log_action(self.request.user, "created", operation, f"Operation created with status '{operation.status}'")

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk=None):
        operation = self.get_object()
        operation.status = 'approved'
        operation.save()
        log_action(request.user, "approved", operation)
        return Response({"status": operation.status})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def reject(self, request, pk=None):
        operation = self.get_object()
        operation.status = 'rejected'
        operation.save()
        log_action(request.user, "rejected", operation)
        return Response({"status": operation.status})

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def execute(self, request, pk=None):
        operation = self.get_object()
        if operation.status != 'approved':
            return Response({"error": "Operation must be approved first"}, status=400)
            # منطق واقعی اجرا (SSH) اینجا اضافه می‌شه
        operation.status = 'executed'
        operation.executed_at = timezone.now()
        operation.save()
        log_action(request.user, "executed", operation, "Operation executed successfully")
        return Response({"status": operation.status})